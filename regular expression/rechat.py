import re
from datetime import datetime

chatbot = 'Jarvis'
created_by='Himanshu'

def process_text(text):
    text = text.lower()  # Convert input to lowercase
    
    if re.search(r'\b(hello|hi|hey|namaste|namaskar)\b', text):
        return "Hello! How can I help you?"

    elif re.search(r'\b(created you| made you)\b', text):
        return f"I was created by {created_by}."    
    
    elif re.search(r'\b(name)\b', text):
        return f"I am your voice assistant, {chatbot}!"
    
    elif re.search(r'\b(time)\b', text):
        return f"The time is {datetime.now().strftime('%H:%M')}."
    
    elif re.search(r'\b(date)\b', text):
        return f"Today is {datetime.now().strftime('%d-%m-%Y')}."
    
    elif re.search(r'\b(month)\b', text):
        return f"It is {datetime.now().strftime('%B')}." # %B is full month name
    
    elif re.search(r'\b(search for|search|google|find|look up)\s+(.*)', text):
        match = re.search(r'\b(search for|google|find|look up)\s+(.*)', text)
        if match:
            #f"Searching for {match}=>Searching for <re.Match object; span=(0, 16), match='google elon musk'>
            #f"Searching for {match.group(2)}" => Searching for elon musk
            return f"Searching for {match.group(2)}..."
        else:
            return "I didn't understand your search query."
    
    elif re.search(r'\b(thank you|thanks)\b', text):
        return "You're welcome! Let me know if you need more help. 😊"
    
    elif re.search(r'\b(exit|bye|quit)\b', text):
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm not sure how to respond to that."

# Run chatbot
if __name__ == '__main__':
    while True:
        user_input = input("You: ")  
        response = process_text(user_input)
        print(f"Jarvis 🤖: {response}")
        
        # Exit condition
        if re.search(r'\b(exit|bye|quit)\b', user_input.lower()):
            break
