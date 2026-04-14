from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

FITNESS_RESPONSES = {
    "home": """🏠 **No-Equipment Home Workout**

**Circuit (3 rounds):**
• 20 Jumping jacks
• 15 Push-ups  
• 20 Bodyweight squats
• 30-second Plank
• 20 Lunges

**Rest:** 60 seconds between rounds
🔥 **Burns ~300 calories!**""",

    "weight": """🎯 **Weight Loss Plan**

**Workouts (5 days/week):**
• HIIT Cardio: 20 min
• Steady State: 30 min walk
• Core Circuit: Crunches, leg raises

**Nutrition:**
• 500 calorie daily deficit
• 1g protein per pound
• Cut sugary drinks!

⚡ **Consistency beats intensity!**""",

    "muscle": """💪 **Muscle Building**

**Push Day:** Bench 4×8, OHP 3×10, Dips 3×fail
**Pull Day:** Deadlifts 4×6, Pull-ups 4×fail, Rows 3×10  
**Legs Day:** Squats 4×8, Leg press 3×12

🥗 **Eat:** 1g protein per pound bodyweight!""",

    "meal": """🥗 **Meal Prep**

**Breakfast:** Oatmeal + protein + berries
**Lunch:** Chicken + quinoa + broccoli  
**Dinner:** Salmon + sweet potato

**Macros:** 40% carbs / 30% protein / 30% fats""",

    "default": """💪 **FitForge AI Tip: Progressive Overload**

Each week:
• Add 2.5 lbs to lifts, OR
• Do 1-2 more reps, OR
• Reduce rest by 15 seconds

Small gains = massive results! 🎯"""
}

def get_response(msg):
    m = msg.lower()
    if "home" in m or "equipment" in m: return FITNESS_RESPONSES["home"]
    if any(x in m for x in ["weight", "lose", "fat"]): return FITNESS_RESPONSES["weight"]
    if any(x in m for x in ["muscle", "bulk", "gain"]): return FITNESS_RESPONSES["muscle"]
    if any(x in m for x in ["meal", "food", "eat"]): return FITNESS_RESPONSES["meal"]
    return FITNESS_RESPONSES["default"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "What's your fitness goal? 💪"})
    time.sleep(0.3)
    return jsonify({"response": get_response(user_input)})

if __name__ == "__main__":
    app.run(debug=True)
