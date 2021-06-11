# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
from utils import evaluate_places
filepath = "birth_places_train.tsv"
predicted_places = ["London" for line in open(filepath).readlines()]
total, correct = evaluate_places(filepath, predicted_places)
print("Correct: ", correct, " out of ", total, ":",str(correct * 100 / total), "%")
