class CropHealth:
    def __init__(self, moisture, temperature):
        self.moisture = moisture
        self.temperature = temperature

    def analyse_health(self):
        if self.moisture < 30:
            return "Health Risk: Low Moisture"
        elif self.temperature > 35:
            return "Health Risk: High Temperature"
        else:
            return "Healthy"

class CareAdvice:
    def __init__(self, crop_health):
        self.crop_health = crop_health

    def generate_care_advice(self):
        health_status = self.crop_health.analyse_health()
        if "Low Moisture" in health_status:
            return "Increase watering frequency"
        elif "High Temperature" in health_status:
            return "Consider shading crops"
        else:
            return "All good. Continue current routine"

# # Create instances and generate advice
# crop = CropHealth(10, 30)
# concern = CareAdvice(crop)
# print(concern.generate_care_advice())


class NutrientDeficiencyDetector:
    def __init__(self, rules):
        # Expecting rules to be a dictionary
        self.deficiency_rules = rules

    def detect(self, leaf_appearance, leaf_stage):
        return self.deficiency_rules.get((leaf_appearance, leaf_stage), "Can't identify the specific issue")

# Define the rules outside the class
rules = {
    ("Yellow all over", "All leaves"): "Your plant has a Nitrogen deficiency. Try mulching with rotted garden compost or manure and monitor results.",
    ("Purplish", "Young leaves"): "Your plant has a Phosphorus deficiency. Flush plants with pH water and nutrients containing phosphorus.",
    ("Yellow Patches", "Old leaves"): "Your plant has a Potassium deficiency. You might want to try organic mulch or some  potassium fertilizer",
    ("Yellow Patches", "Young leaves"): "Your plant has a Magnesium deficiency. Disolve some epsom salts in water and spray on the leaves and around the roots.",
    ("Deformed Leaves", "Young leaves"): "Your plant has a Sulfur deficiency. add sulphur in an inorganic form with a fertilizer containing magnesium, Epsom salts for hydro, and kieserite in soil" ,
}

# Create an instance of the detector with the defined rules
detector = NutrientDeficiencyDetector(rules)

# Example usage
# result = detector.detect("Purplish", "Young leaves")
# print(result)
