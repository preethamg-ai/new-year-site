from flask import Flask

app = Flask(__name__)

common_style = """
<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(120deg, #1a1a1a, #2b2b2b);
    overflow: hidden;
    text-align: center;
    color: #f5f5f5;
}

h1 {
    margin-top: 70px;
    font-size: 42px;
    animation: fadeIn 2s ease-in-out;
}

p {
    font-size: 18px;
    margin: 20px;
    line-height: 1.7;
    animation: fadeIn 3s ease-in-out;
}

.btn {
    padding: 14px 28px;
    font-size: 17px;
    border: none;
    border-radius: 30px;
    background: #ff4d6d;
    color: white;
    cursor: pointer;
    animation: fadeIn 4s ease-in-out;
}

.heart {
    position: absolute;
    color: #ff4d6d;
    font-size: 22px;
    animation: fall 7s linear infinite;
}

@keyframes fall {
    0% { top: -40px; opacity: 1; }
    100% { top: 110%; opacity: 0; }
}

@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}
</style>

<script>
function createHeart() {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (Math.random() * 3 + 5) + "s";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 7000);
}
setInterval(createHeart, 200);
</script>
"""

@app.route("/")
def page1():
    return f"""
    <html>
    <head>{common_style}</head>
    <body>
        <h1>Happy New Year 2025</h1>
        <p>
        Some people stay,<br>
        some become memories,<br>
        but memories… they stay forever.
        </p>
        <button class="btn" onclick="location.href='/page2'">Next ➜</button>
    </body>
    </html>
    """

@app.route("/page2")
def page2():
    return f"""
    <html>
    <head>{common_style}</head>
    <body>
        <h1>💔 From My Heart</h1>
        <p>
        This is not to disturb you,<br>
        not to pull you back,<br>
        just something my heart needed to say once.
        </p>
        <button class="btn" onclick="location.href='/page3'">Read ➜</button>
    </body>
    </html>
    """

@app.route("/page3")
def page3():
    return f"""
    <html>
    <head>
    {common_style}
    <style>
    .sparkle {{
        position: absolute;
        width: 6px;
        height: 6px;
        background: #ffccd5;
        border-radius: 50%;
        animation: sparkle 1.5s linear forwards;
        pointer-events: none;
    }}

    @keyframes sparkle {{
        0% {{ transform: scale(1); opacity: 1; }}
        100% {{ transform: scale(0); opacity: 0; top: -150px; }}
    }}

    .final-text {{
        font-size: 38px;
        color: #ff4d6d;
        margin-top: 40px;
        display: none;
        animation: glow 2s infinite alternate;
    }}

    @keyframes glow {{
        from {{ text-shadow: 0 0 10px #ff758f; }}
        to {{ text-shadow: 0 0 35px #ff4d6d; }}
    }}

    .message {{
        max-width: 900px;
        margin: auto;
        text-align: left;
        padding: 20px;
        font-size: 17px;
    }}
    </style>

    <script>
    function sparkleBurst() {{
        for(let i=0;i<120;i++) {{
            let s = document.createElement("div");
            s.className = "sparkle";
            s.style.left = Math.random() * window.innerWidth + "px";
            s.style.top = Math.random() * window.innerHeight + "px";
            document.body.appendChild(s);
            setTimeout(() => s.remove(), 1500);
        }}
        document.getElementById("finalText").style.display = "block";
        document.getElementById("music").play();
    }}
    </script>
    </head>

    <body>
        <h1>📩 From here my SMS starts</h1>

        <div class="message">
        Hi, this is from your past stupid boy who loved you.  
        Now it is New Year 2025.  
        These 3 years with you… I can’t explain in words.  
        You made my life look better, and thank you for that.

        <br><br>
        Now you are not with me, you are someone else’s.  
        I am sorry to send this. I thought not to…  
        but my heart, you know, it acts mad in your matter.

        <br><br>
        Be happy with who you love and who loves you.  
        Don’t think I will move on —  
        I will stay in memories.  
        Our pictures will never let me forget you.

        <br><br>
        I thought you would be my everything.  
        I lost my dad… my mom loves me a lot, she did nothing less,  
        but when you were with me, I felt complete.  
        Now I lost you too.

        <br><br>
        I feel like no one stays with me for long.  
        It’s New Year and I’m sending a message like this — sorry.

        <br><br>
        Let this new year make you and your loved one happy.  
        Please take care of your health.  
        Don’t take stress.  
        Have a great year.

        <br><br>
        Once again… Happy New Year maa.  
        I don’t know if I have the right to say this,  
        but this will be the last time.

        <br><br>
        I LOVE YOU MY WIFE.  
        Thank you for your time.
        </div>

        <button class="btn" onclick="sparkleBurst()">Finish</button>

        <div id="finalText" class="final-text">
            Happy New Year ❤️
        </div>

        <audio id="music" loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" type="audio/mpeg">
        </audio>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
