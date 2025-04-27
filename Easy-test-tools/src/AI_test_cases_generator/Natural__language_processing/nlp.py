import spacy

nlp = spacy.load("en_core_web_sm")

def extract_test_components(text):
    doc = nlp(text)
    entities = {
        "action": None,    # e.g., "login"
        "condition": None, # e.g., "after 3 attempts"
        "outcome": None    # e.g., "should fail"
    }
    
    # Rule-based extraction (customize as needed)
    for token in doc:
        if token.dep_ == "ROOT":
            entities["action"] = token.text
        if "fail" in token.text.lower():
            entities["outcome"] = "FAIL"
        if token.like_num:  # Extract numbers (e.g., "3 attempts")
            entities["condition"] = token.text
    
    return entities

# Example usage
requirement = "Login should fail after 3 wrong attempts"
components = extract_test_components(requirement)
print(components)
def generate_gherkin(components):
    return f"""
Feature: {components['action']}
  Scenario: {components['condition']} {components['outcome']}
    Given I am on the login page
    When I enter wrong credentials {components['condition']} times
    Then I should see an error message
    """

print(generate_gherkin(components))
def generate_pytest(components):
    return f"""
def test_{components['action'].lower()}_failure():
    for _ in range({components['condition']}):
        enter_wrong_credentials()
    assert is_error_message_displayed()
    """

print(generate_pytest(components))
from transformers import pipeline

test_gen = pipeline("text-generation", model="gpt2")

def ai_generate_test(requirement):
    prompt = f"Generate pytest code for: {requirement}"
    return test_gen(prompt, max_length=100)[0]['generated_text']

print(ai_generate_test("Login should fail after 3 wrong attempts"))