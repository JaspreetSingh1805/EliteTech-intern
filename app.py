from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    classification = None
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height_cm = float(request.form["height"])
            
            # Convert height from cm to meters
            height_m = height_cm / 100.0
            
            # Calculate BMI
            bmi = weight / (height_m ** 2)
            
            # Determine BMI classification
            if bmi < 18.5:
                classification = "Underweight"
            elif 18.5 <= bmi < 24.9:
                classification = "Normal weight"
            elif 25 <= bmi < 29.9:
                classification = "Overweight"
            else:
                classification = "Obesity"
        except ValueError:
            bmi = None

    return render_template("index.html", bmi=bmi, classification=classification)

if __name__ == "__main__":
    app.run(debug=True)
