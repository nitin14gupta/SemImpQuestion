
# Let me analyze all the question papers and extract all questions systematically

question_papers = {
    "2022_December": {
        "Q1A": "Explain the working of DNS with the suitable diagrams. Clearly explain all the steps involved in DNS resolution. (05)",
        "Q1B": "Write a JavaScript code for displaying a digital clock on a web page. (05)",
        "Q1C": "What is Express JS? Explain the advantages of using it. (05)",
        "Q1D": "Explain the event handling in React. Write a React code to create a button 'Greet the User' and display an alert box saying 'Hello!' on clicking that button. (05)",
        "Q2A": "Compare ES 5 and ES 6. Write a code in JavaScript to validate the email address entered by the user (check the presence of '@' character. If this character is missing, the script should display an alert box reporting the error and ask the user to reenter it again). (10)",
        "Q2B": "Explain the concept of Hooks in React. What are the rules for using the Hooks? Write a code making use of React Hooks that displays four buttons namely, 'Red', 'Blue', 'Green', 'Yellow'. On clicking any of these buttons, the code displays the message that you have selected that particular color. (10)",
        "Q3A": "Explain the Document Object Model using a diagram. Write a code in JavaScript for any one of the following: 1) To change the background color of the web page automatically after every 5 seconds. 2) To display three radio buttons on the web page, namely, 'Red', 'Blue' and 'Green'. Selecting any button changes the background color as per the name of the button. (10)",
        "Q3B": "Explain the class components in React. What are the advantages of using them? Demonstrate its use by creating a class for the cars of different models. The component should access the state to display the model of the car on the web page. (10)",
        "Q4A": "What is NodeJs? What are the advantages of using it? Demonstrate the working of NodeJs by creating a simple server to display a 'Welcome' message. (10)",
        "Q4B": "Explain the architecture of NodeJs with a neat diagram. Demonstrate its use by writing the code which creates a simple text file with the data provided by the user. (10)",
        "Q5A": "Demonstrate the routing of web pages using React Router. (05)",
        "Q5B": "Write a JavaScript code to set a cookie on the user's computer. (05)",
        "Q5C": "When are the React components re-rendered? Explain giving examples. (05)",
        "Q5D": "What are the criteria for an API to be a RESTful API? (05)",
        "Q6A": "Explain the MVC architecture with a diagram. What are the advantages of using it? (10)",
        "Q6B": "What is Express used for? Explain the advantages of using Express. What are the different parts of the Express server file? (10)"
    },
    
    "2023_May": {
        "Q1A": "What is HTTP? Explain its working along with request and response example. (05)",
        "Q1B": "Write a Javascript to change the background color of the web page to red color if button named 'RED' is clicked and to green color if button named 'GREEN' is clicked. (05)",
        "Q1C": "Write the program to create a simple HTTP server to display a welcome message with node.js. (05)",
        "Q1D": "What are components in React? Create one class component 'Car' in React and invoke it using index.js. (05)",
        "Q2A": "Write JavaScript to validate Username, Password and Email. Username and Password should not be blank and minimum length of password =8. Email should have @ character. (10)",
        "Q2B": "What is a single page application? Explain React JSX with suitable examples such as rendering the greeting message 'Hello! Welcome to React' (10)",
        "Q3A": "1) Write a Javascript to accept two numbers and display their sum using pop up box. 2) Explain the concept of React Hooks. What are the rules of using Hooks? Write the code making use of Hooks useState function that displays the number of times button named 'CLICK' is clicked. (12)",
        "Q3B": "Explain React Component Life cycle with suitable diagram. (08)",
        "Q4A": "Write an XML file marksheet.xml representing your semester mark sheet. How do you prove that it is well formed and valid XML? (05)",
        "Q4B": "Explain different types of node.js modules? What are different modules that provide core functionality? (05)",
        "Q4C": "What are the features of React.js (05)",
        "Q4D": "Draw and illustrate 3-tier web architecture. (05)",
        "Q5A": "Explain the working of the event loop along with different phases of node.js with a neat diagram. Write an asynchronous file reading node.js program and explain how it is executed. (10)",
        "Q5B": "What is NodeJs and Express.js? Discuss the features and advantages of Express.js. (10)",
        "Q6A": "Explain the architecture of Flux in detail. (10)",
        "Q6B": "Differentiate ES5 and ES6. Give an example of the Anonymous and Arrow function in ES6. (10)"
    },
    
    "2023_December": {
        "Q1A": "Draw and illustrate web 3-tier architecture. (05)",
        "Q1B": "Write a Javascript to accept a number from the user and check if it is even or odd. (05)",
        "Q1C": "Explain React JSX with suitable react examples such as rendering the greeting message 'Hello! Welcome to React' (05)",
        "Q1D": "What is callback in node.js? Give an example. (05)",
        "Q2A": "1) Explain React Component Life cycle with suitable diagram. 2) Write a JavaScript code to set a cookie in the user's computer. (12)",
        "Q2B": "What is a single page application? What are components in React? Create one class component 'Car' in React and invoke it using index.js. (08)",
        "Q3A": "Write the code to process online Alumni information for your college. Create a form to get a name, date of birth and email id. Use check boxes for taking hobbies and radio buttons for selecting branch. Write JavaScript code to validate the following. -User has to fill all the fields prior to the form submission. -Valid email id (@ and .) -Age validation using DOB (>=22 years) (10)",
        "Q3B": "Explain the concept of React Hooks. What are the rules of using Hooks? Write the code making use of Hooks useState function that displays the number of times a button named 'CLICK' is clicked. (10)",
        "Q4A": "Write a short note on Document Object Model(DOM) (05)",
        "Q4B": "Explain different types of node.js modules? What are different modules that provide core functionality? (05)",
        "Q4C": "What are the features of React.js (05)",
        "Q4D": "Write a Javascript Program that changes the background color of page by refreshing the page every 2 seconds (05)",
        "Q5A": "Explain the architecture of node.js with a neat diagram. Write an asynchronous file reading node.js program and explain how it is executed. (10)",
        "Q5B": "What is NodeJs and Express.js? Discuss the features and advantages of Express.js. Explain cookies concept in Express.js with example. (10)",
        "Q6A": "Differentiate between MVC, FLUX and Redux. (10)",
        "Q6B": "Differentiate between ES5 and ES6. Describe the concepts of Arrow Functions, classes and inheritance in JavaScript. (10)"
    },
    
    "2024_May": {
        "Q1A": "Explain how DNS works and the process it follows to resolve domain names to IP addresses. (05)",
        "Q1B": "Differentiate between JSON and XML. Discuss their use cases and advantages in web development. (05)",
        "Q1C": "Illustrate with an example how to handle form validation in JavaScript, including client-side validation for an email and password field. (05)",
        "Q1D": "Create a simple React application that fetches data from an external API and displays it in a list format. Describe the steps involved. (05)",
        "Q2A": "Discuss the asynchronous nature of JavaScript and how Promises and async/await improve handling of asynchronous operations. Provide code examples (10)",
        "Q2B": "Explain the concept of state and props in React. How do they differ, and how are they used in components? (10)",
        "Q3A": "Compare and contrast the use of classes and inheritance in JavaScript with functional programming paradigms. Provide examples. (10)",
        "Q3B": "Create a simple Express application that integrates with React to display a list of items fetched from a server. Describe the steps involved and provide code snippets. (10)",
        "Q4A": "Explain how React's useEffect hook can be used to perform side effects in functional components. Provide an example where useEffect is used to fetch data from an API and display it in a component. (10)",
        "Q4B": "Create a web page using HTML and JavaScript where an image moves across the screen from left to right continuously. Provide the HTML and JavaScript code and explain the implementation. (10)",
        "Q5A": "Describe the Event Loop in Node.js. How does it handle asynchronous operations? Provide an example. (10)",
        "Q5B": "Explain how React Router can be used to create a single-page application (SPA). Provide an example of routing in React. (10)",
        "Q6A": "Describe how to manage state in a React application using Redux. Include an example to illustrate state management in a complex application. (10)",
        "Q6B": "Explain how Node.js handles asynchronous operations using callbacks, Promises, and async/await. Provide code examples for each method. (10)"
    },
    
    "2024_December": {
        "Q1A": "Explain the role of XML and JS in web communication. (06)",
        "Q1B": "Describe the differences between XML and JSON with examples. (06)",
        "Q1C": "Discuss the lifecycle of a React component and its significance in single-page applications. (06)",
        "Q1D": "Given a scenario where a Node.js application has to handle multiple client requests asynchronously, outline the best practices to manage the callback functions effectively. (06)",
        "Q2A": "Write a JavaScript program to validate an email input form. Include error handling for invalid formats. (10)",
        "Q2B": "Explain the purpose of Express Router and how it aids in organizing route handling in a Node.js application. (10)",
        "Q3A": "Illustrate the use of State and Props in React with a practical example demonstrating their interaction. (10)",
        "Q3B": "Develop a simple program in Node.js to read data from a file and send it as a response to an HTTP request. Explain the key steps in the code. (10)",
        "Q4A": "You are tasked to design a form validation system in JavaScript for a signup form with username, password, and email fields. Explain how you would implement this with error handling and ensure data security. (10)",
        "Q4B": "Create a React component using functional components and Hooks to display a list of items that a user can add to or remove from. Describe how the useState and useEffect hooks are used in your solution. (10)",
        "Q5A": "Describe how REST APIs function in web development and provide an example of an HTTP GET request. (10)",
        "Q5B": "Write a React component to render a form and handle its submit event. The form should capture user inputs and display a confirmation message upon submission. (10)",
        "Q6A": "Explain the architecture of Flux in detail. (10)",
        "Q6B": "Develop a Node.js application that uses streams to read and write data efficiently. Describe the scenarios where using streams is preferable over other data-handling techniques. (10)"
    },
    
    "2025_May": {
        "Q1A": "What is DNS? Explain the working of DNS with its components. (05)",
        "Q1B": "Write a JavaScript function that validates: Username (alphanumeric, 5-15 characters), Password (minimum 8 characters, must contain uppercase, lowercase, and number) (05)",
        "Q1C": "Explain the concepts of Arrow Functions in JavaScript ES6 with examples. (05)",
        "Q1D": "What is a callback in Node.js? Explain with a suitable example. (05)",
        "Q2A": "Explain Document Object Model (DOM) and its levels. Write a JavaScript program that accepts two numbers as input and displays their sum. (10)",
        "Q2B": "What is React.js? Discuss different features and advantages of React.js. What are components in React? Give examples. (10)",
        "Q3A": "Explain different types of Node.js modules. What are the modules that provide core functionality? (10)",
        "Q3B": "Write a stepwise process to create an APP using ReactJS to print 'Hello World'. (10)",
        "Q4A": "Compare and contrast MVC, FLUX, and Redux architectures. Explain their use in modern web applications. (10)",
        "Q4B": "Write a Node.js program using Express to create a basic server that: Handles GET and POST requests, Implements basic routing, Includes error handling. Provide complete code with explanations. (10)",
        "Q5A": "Explain the concept of React Hooks. What are the rules of using Hooks? Provide examples of useState and useEffect. (10)",
        "Q5B": "What is ExpressJS? Explain features of ExpressJS. (10)",
        "Q6A": "Describe the architecture of Node.js with a neat diagram. Explain its event-driven programming model. (10)",
        "Q6B": "Write JavaScript code to process an online form with the following validations: All fields must be filled, Email must contain '@' and '.', Age must be between 18 and 60. Include proper error messages and form submission handling. (10)"
    }
}

# Now let's analyze frequency of topics
topic_frequency = {}

# Core topics mapping
topics = {
    "DNS": ["DNS", "domain name"],
    "JavaScript Validation": ["validate", "validation", "form validation"],
    "React Hooks": ["Hooks", "useState", "useEffect"],
    "Node.js Architecture": ["architecture of node", "node.js architecture"],
    "Express.js": ["Express", "ExpressJS"],
    "React Components": ["components in React", "class component", "functional component"],
    "Event Loop": ["event loop", "asynchronous"],
    "DOM": ["Document Object Model", "DOM"],
    "React Lifecycle": ["lifecycle", "component lifecycle"],
    "State and Props": ["state and props", "state", "props"],
    "ES5 vs ES6": ["ES5 and ES6", "ES6", "Arrow Functions"],
    "MVC/FLUX/Redux": ["MVC", "FLUX", "Redux"],
    "React Router": ["React Router", "routing"],
    "JSX": ["JSX", "React JSX"],
    "Callbacks": ["callback", "callbacks"],
    "HTTP/REST": ["HTTP", "REST", "RESTful"],
    "XML/JSON": ["XML", "JSON"],
    "3-tier Architecture": ["3-tier", "web architecture"],
    "Cookies": ["cookie", "cookies"],
    "Promises/Async-Await": ["Promise", "async/await"],
    "File Operations": ["file", "read data", "write data"],
    "React useEffect": ["useEffect"],
    "Single Page Application": ["single page application", "SPA"]
}

# Count topic frequencies
for year_paper, questions in question_papers.items():
    for qid, question in questions.items():
        question_lower = question.lower()
        for topic, keywords in topics.items():
            for keyword in keywords:
                if keyword.lower() in question_lower:
                    if topic not in topic_frequency:
                        topic_frequency[topic] = 0
                    topic_frequency[topic] += 1
                    break

# Sort by frequency
sorted_topics = sorted(topic_frequency.items(), key=lambda x: x[1], reverse=True)

print("=" * 80)
print("TOPIC FREQUENCY ANALYSIS (Most Important Topics)")
print("=" * 80)
for i, (topic, freq) in enumerate(sorted_topics, 1):
    print(f"{i:2d}. {topic:30s} - Appeared {freq} times")

print("\n" + "=" * 80)
print("SUMMARY: Total unique topics analyzed:", len(sorted_topics))
print("=" * 80)
