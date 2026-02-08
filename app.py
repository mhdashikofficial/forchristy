# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>To My Catwoman ♡</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;500;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS v4 Play CDN -->
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  
  <style type="text/tailwindcss">
    @theme {
      --font-sans: 'Poppins', system-ui, sans-serif;
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-script: 'Great Vibes', cursive;
    }
  </style>

  <style>
    .heart {
      position: absolute;
      font-size: 1.5rem;
      pointer-events: none;
      user-select: none;
      animation: rise linear forwards;
      will-change: transform, opacity;
    }
    @keyframes rise {
      0%   { transform: translateY(120vh) scale(0.3) rotate(0deg); opacity: 0.8; }
      30%  { opacity: 1; }
      100% { transform: translateY(-40vh) scale(1.4) rotate(1080deg); opacity: 0; }
    }
    .message {
      opacity: 0;
      transform: translateY(30px);
      transition: all 1.1s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .message.visible {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-indigo-950 via-purple-950 to-pink-950 text-white overflow-hidden relative font-sans">

  <!-- Floating hearts container -->
  <div id="hearts" class="fixed inset-0 pointer-events-none z-10 overflow-hidden"></div>

  <div class="relative z-20 min-h-screen flex items-center justify-center p-6">
    <div class="w-full max-w-2xl bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-2xl shadow-black/60 p-10 md:p-14
                transition-all duration-700 hover:shadow-pink-500/20 hover:border-pink-500/30">

      <h1 class="text-6xl md:text-8xl font-script text-center text-pink-500 drop-shadow-lg animate-pulse-slow">
        Christina ♡
      </h1>
      
      <p class="text-2xl md:text-3xl font-serif text-center text-pink-300 mt-3 mb-12 opacity-90">
        My Catwoman • My Safe Place • My Forever
      </p>

      <div id="messages" class="space-y-10 text-lg md:text-xl leading-relaxed text-gray-100">
        <div id="m1" class="message">
          Christy… you walked into my life when everything felt wrong — fake smiles, empty promises, people who never truly cared.<br><br>
          And then <span class="text-pink-400 font-medium">you</span> arrived… the most real thing I’ve ever known.
        </div>

        <div id="m2" class="message">
          Your care felt real. Your presence felt like peace.<br><br>
          For the first time, I understood what “home” actually means.
        </div>

        <div id="m3" class="message">
          You’re the one I want to hold close — today, tomorrow, and every day after.<br><br>
          Whenever I get even the smallest chance to make you happy, I pour my whole heart into it.
        </div>

        <div id="m4" class="message">
          The moment you said yes and became mine…<br>
          it felt like the universe finally smiled back and whispered:<br>
          “He waited long enough — give him her.”
        </div>

        <div id="m5" class="message">
          When the world turns loud, cold and competitive…<br>
          you remain my quiet, warm, safe place.<br>
          My only true <span class="text-pink-400 font-medium">home</span>.
        </div>

        <div id="m6" class="message">
          My love for you goes so much deeper than these words can ever show.<br><br>
          You’re already mine… but today — on Propose Day —<br>
          I want to kneel in my heart and ask you once more:
        </div>

        <div id="m7" class="message text-center text-2xl md:text-3xl font-medium text-pink-300 pt-8">
          <strong>Christina, my breathtaking Catwoman…<br>
          will you be my Valentine again — and always?</strong>
        </div>
      </div>

      <div class="mt-12 text-center">
        <button id="nextBtn" 
                class="px-10 py-5 bg-gradient-to-r from-pink-600 to-rose-600 hover:from-pink-500 hover:to-rose-500 
                       text-white font-medium text-xl rounded-full shadow-lg shadow-pink-700/40 
                       transform transition-all duration-300 hover:scale-110 hover:shadow-2xl active:scale-95">
          Next ♡
        </button>

        <button id="yesBtn" 
                class="px-12 py-6 bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-400 hover:to-purple-500 
                       text-white font-medium text-2xl rounded-full shadow-xl shadow-pink-700/50 hidden
                       transform transition-all duration-300 hover:scale-110 hover:shadow-2xl active:scale-95">
          Yes, forever ♡
        </button>
      </div>
    </div>
  </div>

<script>
// Floating hearts
function createHeart() {
  const heart = document.createElement('div');
  heart.className = 'heart';
  heart.innerHTML = ['♡','💗','💞','💖','❤️','🫀'][Math.floor(Math.random()*6)];
  heart.style.left = Math.random() * 100 + 'vw';
  heart.style.animationDuration = (Math.random() * 7 + 9) + 's';
  heart.style.fontSize = (Math.random() * 1.8 + 1.2) + 'rem';
  heart.style.transform = `rotate(${Math.random()*60 - 30}deg)`;
  document.getElementById('hearts').appendChild(heart);
  setTimeout(() => heart.remove(), 15000);
}
setInterval(createHeart, 420);

// Message reveal
const messages = document.querySelectorAll('#messages .message');
const nextBtn = document.getElementById('nextBtn');
const yesBtn = document.getElementById('yesBtn');
let index = -1;

function showNext() {
  if (index >= messages.length - 1) return;
  index++;
  messages[index].classList.add('visible');

  if (index === messages.length - 1) {
    nextBtn.classList.add('hidden');
    setTimeout(() => {
      yesBtn.classList.remove('hidden');
      yesBtn.classList.add('animate-pulse');
    }, 1600);
  }
}

nextBtn.addEventListener('click', showNext);

// Yes celebration
yesBtn.addEventListener('click', () => {
  const card = document.querySelector('.max-w-2xl');
  card.innerHTML = `
    <div class="text-center py-20">
      <h1 class="text-8xl md:text-10xl font-script text-pink-400 animate-bounce">YESSSS!!! ♡</h1>
      <p class="text-4xl md:text-6xl font-serif text-pink-200 mt-10">
        I love you forever, my Catwoman
      </p>
      <p class="text-2xl text-gray-300 mt-8">
        Thank you for being my home.<br>
        Here's to us — always and endlessly ♡
      </p>
    </div>
  `;
  card.classList.add('bg-gradient-to-br', 'from-pink-900', 'via-purple-900', 'to-rose-950');

  // Massive heart rain
  for (let i = 0; i < 120; i++) {
    setTimeout(createHeart, i * 50);
  }
  setInterval(createHeart, 200);
});

showNext(); // Start with first message
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

if __name__ == '__main__':
    app.run(debug=True)
