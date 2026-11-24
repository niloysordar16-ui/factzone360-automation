
import requests
import os

def generate_facts(topic):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Please set your Gemini API key.")
        return

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-2.5-flash:generateContent"
        f"?key={api_key}"
    )

    prompt = f"""
    Create 5 amazing facts about {topic}.
    Write in simple Bengali.
    Make each fact suitable for an Instagram Reel.
    Include a catchy opening and ending.
    """

    response = requests.post(
        url,
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=60
    )

    if response.ok:
        result = response.json()
        text = result["candidates"][0]["content"]["parts"][0]["text"]

        with open("facts.txt", "w", encoding="utf-8") as file:
            file.write(text)

        print(text)
        print("\nFacts saved successfully!")
    else:
        print("API Error:", response.text)


if __name__ == "__main__":
    topic = input("Enter your fact topic: ")
    generate_facts(topic)

