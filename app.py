# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CONTENT = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Debug - Christina Proposal</title>
  
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display&family=Poppins&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  
  <style>
    body { 
      background: linear-gradient(to bottom right, #1a0033, #33001a);
      color: white;
      font-family: 'Poppins', sans-serif;
      min-height: 100vh;
      margin: 0;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .card {
      background: rgba(30, 10, 50, 0.7);
      backdrop-filter: blur(10px);
      border: 2px solid #ff4d88;
      border-radius: 20px;
      padding: 30px;
      max-width: 700px;
      width: 90%;
      margin: 20px auto;
      text-align: center;
    }
    h1 { font-family: 'Great Vibes', cursive; font-size: 5.5rem; color: #ff66aa; margin: 0; }
    .subtitle { font-family: 'Playfair Display', serif; font-size: 2rem; color: #ff99cc; }
    .message { font-size: 1.4rem; line-height: 1.7; margin: 25px 0; min-height: 120px; }
    #buttons { 
      margin-top: 40px; 
      display: block !important; 
      visibility: visible !important; 
    }
    #nextBtn {
      background: linear-gradient(to right, #ffeb3b, #ffc107) !important;
      color: black !important;
      font-size: 2rem !important;
      padding: 20px 60px !important;
      border-radius: 9999px;
      border: 3px solid #ff4081;
      box-shadow: 0 10px 30px rgba(255, 193, 7, 0.7);
      cursor: pointer;
      display: inline-block !important;
      visibility: visible !important;
    }
    #nextBtn:hover { transform: scale(1.1); background: white !important; }
    .hidden { display: none; }
  </style>
</head>
<body>

<div class="card">
  <h1>Christina ♡</h1>
  <div class="subtitle">My Catwoman • My Home</div>
  
  <div id="messages">
    <div class="message" id="m1">
      Christy, you came into my life when everything was feeling off and wrong — fake people, fake care.<br><br>
      Then you entered as the most real person I've ever seen...
    </div>
  </div>

  <div id="buttons">
    <button id="nextBtn">NEXT ♡ (should be VERY visible)</button>
    <button id="yesBtn" class="hidden" style="background: #22c55e; color: white; font-size: 2rem; padding: 20px 60px; border-radius: 9999px; margin-top: 20px;">
      YES forever ♡
    </button>
  </div>

  <p style="color: #ffeb3b; font-size: 1.5rem; margin-top: 30px; font-weight: bold;">
    DEBUG: If you don't see a big yellow button above → tell me what you see instead
  </p>
</div>

<script>
// Simple console debug
console.log("Script running");
const nextBtn = document.getElementById('nextBtn');
const yesBtn = document.getElementById('yesBtn');
console.log("nextBtn element:", nextBtn);

if (nextBtn) {
  console.log("Button found — should be visible");
  nextBtn.style.display = 'inline-block';
} else {
  console.log("Button NOT found in DOM!");
}

// Click handler (minimal)
nextBtn.addEventListener('click', () => {
  alert("Next clicked! If you see this → JS is working");
  // You can add more messages later — keeping simple for debug
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
