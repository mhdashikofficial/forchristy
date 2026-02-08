# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CONTENT = r"""
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>To My Catwoman ♡</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;500;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            script: ['Great Vibes', 'cursive'],
            serif: ['Playfair Display', 'serif'],
            sans: ['Poppins', 'sans-serif'],
          }
        }
      }
    }
  </script>

  <style>
    .heart {
      position: absolute;
      font-size: 1.8rem;
      pointer-events: none;
      user-select: none;
      animation: rise linear forwards;
      will-change: transform, opacity;
    }
    @keyframes rise {
      0%   { transform: translateY(120vh) scale(0.4) rotate(0deg); opacity: 0.7; }
      25%  { opacity: 1; }
      100% { transform: translateY(-50vh) scale(1.3) rotate(1440deg); opacity: 0; }
    }
    .message {
      opacity: 0;
      transform: translateY(30px);
      transition: all 1.1s ease-out;
    }
    .message.visible {
      opacity: 1;
      transform: translateY(0);
    }
    #nextBtn {
      transition: all 0.3s ease;
    }
    #nextBtn:hover, #yesBtn:hover {
      transform: scale(1.08) translateY(-3px);
      box-shadow: 0 20px 40px -10px rgba(236, 72, 153, 0.7) !important;
      filter: brightness(1.15);
    }
  </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-[#0f001a] via-[#1a000f] to-[#2a0015] text-white overflow-hidden relative font-sans">

  <div id="hearts" class="fixed inset-0 pointer-events-none z-10 overflow-hidden"></div>

  <div class="relative z-20 min-h-screen flex items-center justify-center p-6">
    <div class="w-full max-w-2xl bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-2xl shadow-black/70 p-10 md:p-14">

      <h1 class="text-6xl md:text-8xl font-script text-center text-pink-500 drop-shadow-lg">
        Christina ♡
      </h1>
      
      <p class="text-2xl md:text-3xl font-serif text-center text-pink-300 mt-4 mb-10 opacity-90">
        My Catwoman • My Home • My Forever
      </p>

      <div id="messages" class="space-y-10 text-lg md:text-xl leading-relaxed text-gray-100">
        <div id="m1" class="message visible">  <!-- First one visible by default -->
          Christy, you came into my life when everything was feeling off and wrong — fake people, fake care.<br><br>
          Then you entered as the most real person I've ever seen in my life… with some real care.
        </div>

        <div id="m2" class="message">
          You became something that finally made me feel like I have a home.<br><br>
          Something I want to hold lifelong with me.
        </div>

        <div id="m3" class="message">
          Whenever I get a chance to do something for you, I really try my best to utilize it better.<br><br>
          And the moment I got the chance to be your boyfriend was my favourite moment with you.
        </div>

        <div id="m4" class="message">
          It was like finally God saw my efforts and chose me for you.<br><br>
          I'm not making this over-dramatic — all this is straight from my thoughts and heart.
        </div>

        <div id="m5" class="message">
          When the world feels competitive and heavy, giving me tough competition…<br>
          you're the only place I feel comfortable and home.
        </div>

        <div id="m6" class="message">
          I do love you more than the words I wrote here.<br><br>
          You're already mine… but as it's Propose Day, I'm proposing you again:
        </div>

        <div id="m7" class="message text-center text-2xl md:text-3xl font-medium text-pink-300 pt-8 pb-6">
          <strong>Christina (my beautiful Catwoman),<br>will you be my Valentine… again and always?</strong>
        </div>
      </div>

      <div id="buttons" class="mt-12 text-center">
        <button id="nextBtn" 
                class="px-10 py-5 bg-gradient-to-r from-pink-600 to-rose-600 text-white font-medium text-xl rounded-full shadow-lg shadow-pink-800/50">
          Next ♡
        </button>

        <button id="yesBtn" 
                class="px-12 py-6 bg-gradient-to-r from-pink-500 to-purple-600 text-white font-medium text-2xl rounded-full shadow-xl shadow-pink-800/60 hidden">
          Yes, forever ♡
        </button>
      </div>
    </div>
  </div>

<script>
// Hearts
function createHeart() {
  const h = document.createElement('div');
  h.className = 'heart';
  h.innerHTML = ['♡','💗','💞','💖','❤️','🫶'][Math.floor(Math.random()*6)];
  h.style.left = Math.random()*100 + 'vw';
  h.style.animationDuration = (Math.random()*8 + 10)+'s';
  h.style.fontSize = (Math.random()*2 + 1.3)+'rem';
  document.getElementById('hearts').appendChild(h);
  setTimeout(()=>h.remove(), 16000);
}
setInterval(createHeart, 500);

// Messages
const messages = document.querySelectorAll('#messages .message');
const nextBtn = document.getElementById('nextBtn');
const yesBtn = document.getElementById('yesBtn');
let index = 0;  // first is already visible

function showNext() {
  if (index >= messages.length - 1) return;
  
  index++;
  messages[index].classList.add('visible');
  
  if (index === messages.length - 1) {
    setTimeout(() => {
      nextBtn.classList.add('hidden');
      yesBtn.classList.remove('hidden');
    }, 1400);
  }
}

nextBtn.addEventListener('click', showNext);

// Force button visibility (extra safety)
window.addEventListener('load', () => {
  document.getElementById('buttons').style.display = 'block';
  nextBtn.style.display = 'inline-block';
});

// Yes celebration
yesBtn.addEventListener('click', () => {
  document.querySelector('.max-w-2xl').innerHTML = `
    <div class="text-center py-20">
      <h1 class="text-8xl md:text-[10rem] font-script text-pink-400 animate-bounce">YESSSS!!! ♡</h1>
      <p class="text-5xl md:text-7xl font-serif text-pink-200 mt-10">I love you forever, my Catwoman</p>
      <p class="text-2xl text-gray-200 mt-8">Thank you for being my home.<br>Here's to us — always ♡</p>
    </div>
  `;
  // Heart rain
  for(let i=0; i<120; i++) setTimeout(createHeart, i*60);
  setInterval(createHeart, 250);
});
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

if __name__ == '__main__':
    app.run(debug=True)
