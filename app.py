# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>To My Catwoman ♡</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@400;500;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body {
      min-height: 100vh;
      background: linear-gradient(135deg, #0f001a 0%, #1a000f 50%, #2a0015 100%);
      color: #fff;
      font-family: 'Poppins', sans-serif;
      overflow: hidden;
      position: relative;
    }
    #hearts {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
    }
    .heart {
      position: absolute;
      font-size: 1.8rem;
      pointer-events: none;
      animation: rise linear forwards;
    }
    @keyframes rise {
      0%   { transform: translateY(110vh) scale(0.4) rotate(0deg); opacity: 0.8; }
      30%  { opacity: 1; }
      100% { transform: translateY(-40vh) scale(1.3) rotate(1080deg); opacity: 0; }
    }
    .container {
      position: relative;
      z-index: 10;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .card {
      background: rgba(25, 8, 45, 0.7);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 50, 120, 0.25);
      border-radius: 28px;
      padding: 3rem 2.5rem;
      max-width: 680px;
      width: 100%;
      box-shadow: 0 20px 70px rgba(0,0,0,0.65);
    }
    h1 {
      font-family: 'Great Vibes', cursive;
      font-size: 6rem;
      color: #ff3366;
      text-align: center;
      text-shadow: 0 0 25px rgba(255, 51, 102, 0.6);
      margin-bottom: 0.8rem;
    }
    .subtitle {
      font-family: 'Playfair Display', serif;
      font-size: 2.1rem;
      color: #ff99cc;
      text-align: center;
      margin-bottom: 2.5rem;
      opacity: 0.92;
    }
    .message {
      font-size: 1.25rem;
      line-height: 1.85;
      margin: 2rem 0;
      opacity: 0;
      transform: translateY(35px);
      transition: all 1.15s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .message.visible {
      opacity: 1;
      transform: translateY(0);
    }
    .btn-container {
      text-align: center;
      margin-top: 2.5rem;
    }
    .btn {
      background: linear-gradient(45deg, #ff1e56, #ff5e78);
      color: white;
      font-size: 1.35rem;
      font-weight: 500;
      padding: 1.1rem 3.2rem;
      border: none;
      border-radius: 999px;
      cursor: pointer;
      box-shadow: 0 12px 35px rgba(255, 30, 86, 0.45);
      transition: all 0.35s ease;
    }
    .btn:hover {
      transform: scale(1.08) translateY(-4px);
      box-shadow: 0 22px 50px rgba(255, 30, 86, 0.65);
      filter: brightness(1.12);
    }
    .btn.yes {
      background: linear-gradient(45deg, #c026d3, #a855f7);
      box-shadow: 0 12px 35px rgba(168, 85, 247, 0.5);
    }
    .btn.yes:hover {
      box-shadow: 0 22px 50px rgba(168, 85, 247, 0.7);
    }
    .hidden { display: none !important; }
  </style>
</head>
<body>

<div id="hearts"></div>

<div class="container">
  <div class="card">
    <h1>Christina ♡</h1>
    <div class="subtitle">My Catwoman • My Home • My Forever</div>

    <div id="messages">
      <div class="message visible">
        Christy, you came into my life when everything was feeling off and wrong — fake people, fake care.<br><br>
        Then you entered as the most real person I've ever seen in my life… with some real care.
      </div>

      <div class="message">
        You became something that finally made me feel like I have a home.<br><br>
        Something I want to hold lifelong with me.
      </div>

      <div class="message">
        Whenever I get a chance to do something for you, I really try my best to utilize it better.<br><br>
        And the moment I got the chance to be your boyfriend was my favourite moment with you.
      </div>

      <div class="message">
        It was like finally God saw my efforts and chose me for you.<br><br>
        I'm not making this over-dramatic — all this is straight from my thoughts and heart.
      </div>

      <div class="message">
        When the world feels competitive and heavy, giving me tough competition…<br>
        you're the only place I feel comfortable and home.
      </div>

      <div class="message">
        I do love you more than the words I wrote here.<br><br>
        You're already mine… but as it's Propose Day, I'm proposing you again:
      </div>

      <div class="message text-center" style="font-size: 1.6rem; font-weight: 500; color: #ff99cc; padding-top: 1.5rem;">
        <strong>Christina (my beautiful Catwoman),<br>will you be my Valentine… again and always?</strong>
      </div>
    </div>

    <div class="btn-container">
      <button id="nextBtn" class="btn">Next ♡</button>
      <button id="yesBtn" class="btn yes hidden">Yes, forever ♡</button>
    </div>
  </div>
</div>

<script>
// Floating hearts
function createHeart() {
  const heart = document.createElement('div');
  heart.className = 'heart';
  heart.innerHTML = ['♡','💗','💞','💖','❤️','🫶'][Math.floor(Math.random()*6)];
  heart.style.left = Math.random() * 100 + 'vw';
  heart.style.animationDuration = (Math.random() * 7 + 9) + 's';
  heart.style.fontSize = (Math.random() * 2.2 + 1.4) + 'rem';
  heart.style.transform = `rotate(${Math.random()*90 - 45}deg)`;
  document.getElementById('hearts').appendChild(heart);
  setTimeout(() => heart.remove(), 14000);
}
setInterval(createHeart, 480);

// Message reveal
const messages = document.querySelectorAll('#messages .message');
const nextBtn = document.getElementById('nextBtn');
const yesBtn = document.getElementById('yesBtn');
let current = 0;  // first one already visible

function showNext() {
  if (current >= messages.length - 1) return;
  current++;
  messages[current].classList.add('visible');

  if (current === messages.length - 1) {
    setTimeout(() => {
      nextBtn.classList.add('hidden');
      yesBtn.classList.remove('hidden');
    }, 1600);
  }
}

nextBtn.addEventListener('click', showNext);

// Yes celebration
yesBtn.addEventListener('click', () => {
  document.querySelector('.card').innerHTML = `
    <h1 style="font-size: 8rem; margin: 2rem 0;">YESSSS!!! ♡</h1>
    <div style="font-size: 3.2rem; color: #ff99cc; margin: 2rem 0; font-family: 'Great Vibes', cursive;">
      I love you forever, my Catwoman
    </div>
    <div style="font-size: 1.6rem; opacity: 0.9;">
      Thank you for being my home.<br>
      Here's to us — always and endlessly ♡
    </div>
  `;
  // Heart explosion
  for (let i = 0; i < 140; i++) {
    setTimeout(createHeart, i * 45);
  }
  setInterval(createHeart, 220);
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
