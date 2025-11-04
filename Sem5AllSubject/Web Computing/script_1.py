
# Now let's create a comprehensive list of top 25-30 most important questions based on frequency and importance

important_questions = [
    {
        "no": 1,
        "topic": "Express.js",
        "question": "What is Express.js? Explain the features and advantages of using Express. What are the different parts of the Express server file?",
        "marks": "10"
    },
    {
        "no": 2,
        "topic": "JavaScript Form Validation",
        "question": "Write JavaScript code to validate Username, Password and Email with following conditions: Username and Password should not be blank, minimum length of password = 8 with uppercase, lowercase and number, Email should have @ and . character.",
        "marks": "10"
    },
    {
        "no": 3,
        "topic": "React State and Props",
        "question": "Explain the concept of state and props in React. How do they differ, and how are they used in components? Illustrate with practical examples.",
        "marks": "10"
    },
    {
        "no": 4,
        "topic": "React Hooks - useState & useEffect",
        "question": "Explain the concept of React Hooks. What are the rules of using Hooks? Provide examples of useState and useEffect hooks.",
        "marks": "10"
    },
    {
        "no": 5,
        "topic": "Node.js Architecture",
        "question": "Explain the architecture of Node.js with a neat diagram. Explain its event-driven programming model.",
        "marks": "10"
    },
    {
        "no": 6,
        "topic": "React Components",
        "question": "What are components in React? Explain class components and functional components. Create a class component 'Car' in React and demonstrate its use.",
        "marks": "10"
    },
    {
        "no": 7,
        "topic": "Node.js File Operations",
        "question": "Write a Node.js program to create a simple text file with data provided by the user. Explain asynchronous file reading in Node.js.",
        "marks": "10"
    },
    {
        "no": 8,
        "topic": "MVC, FLUX and Redux",
        "question": "Compare and contrast MVC, FLUX, and Redux architectures. Explain their use in modern web applications.",
        "marks": "10"
    },
    {
        "no": 9,
        "topic": "Event Loop in Node.js",
        "question": "Explain the working of the event loop along with different phases of Node.js with a neat diagram. How does it handle asynchronous operations?",
        "marks": "10"
    },
    {
        "no": 10,
        "topic": "DNS Working",
        "question": "What is DNS? Explain the working of DNS with suitable diagrams. Clearly explain all the steps involved in DNS resolution.",
        "marks": "05"
    },
    {
        "no": 11,
        "topic": "Document Object Model (DOM)",
        "question": "Explain the Document Object Model (DOM) and its levels. Write a JavaScript program that accepts two numbers as input and displays their sum.",
        "marks": "10"
    },
    {
        "no": 12,
        "topic": "HTTP Protocol",
        "question": "What is HTTP? Explain its working along with request and response examples. Explain REST APIs and HTTP GET/POST requests.",
        "marks": "05"
    },
    {
        "no": 13,
        "topic": "React JSX",
        "question": "What is React JSX? Explain React JSX with suitable examples such as rendering the greeting message 'Hello! Welcome to React'.",
        "marks": "05"
    },
    {
        "no": 14,
        "topic": "Node.js Callbacks",
        "question": "What is a callback in Node.js? Explain with suitable examples. Discuss callback functions and best practices to manage them effectively.",
        "marks": "05"
    },
    {
        "no": 15,
        "topic": "XML vs JSON",
        "question": "Differentiate between JSON and XML. Discuss their use cases and advantages in web development.",
        "marks": "05"
    },
    {
        "no": 16,
        "topic": "React Router",
        "question": "Explain how React Router can be used to create a single-page application (SPA). Demonstrate the routing of web pages using React Router.",
        "marks": "10"
    },
    {
        "no": 17,
        "topic": "Express Server with Routing",
        "question": "Write a Node.js program using Express to create a basic server that handles GET and POST requests, implements basic routing, and includes error handling.",
        "marks": "10"
    },
    {
        "no": 18,
        "topic": "React Component Lifecycle",
        "question": "Explain React Component Lifecycle with suitable diagram. When are the React components re-rendered?",
        "marks": "10"
    },
    {
        "no": 19,
        "topic": "Single Page Application",
        "question": "What is a single page application (SPA)? Explain its advantages and how React facilitates building SPAs.",
        "marks": "05"
    },
    {
        "no": 20,
        "topic": "Node.js Modules",
        "question": "Explain different types of Node.js modules. What are the modules that provide core functionality?",
        "marks": "05"
    },
    {
        "no": 21,
        "topic": "ES5 vs ES6",
        "question": "Differentiate between ES5 and ES6. Explain the concepts of Arrow Functions, classes and inheritance in JavaScript ES6 with examples.",
        "marks": "10"
    },
    {
        "no": 22,
        "topic": "JavaScript Cookies",
        "question": "Write a JavaScript code to set a cookie on the user's computer. Explain cookies concept in Express.js with example.",
        "marks": "05"
    },
    {
        "no": 23,
        "topic": "3-Tier Web Architecture",
        "question": "Draw and illustrate 3-tier web architecture. Explain each tier and its role in web applications.",
        "marks": "05"
    },
    {
        "no": 24,
        "topic": "Promises and Async/Await",
        "question": "Discuss the asynchronous nature of JavaScript. Explain how Node.js handles asynchronous operations using callbacks, Promises, and async/await with code examples.",
        "marks": "10"
    },
    {
        "no": 25,
        "topic": "JavaScript DOM Manipulation",
        "question": "Write JavaScript code to change the background color of a web page (automatically every 5 seconds OR using buttons). Also, write code for displaying a digital clock.",
        "marks": "05"
    },
    {
        "no": 26,
        "topic": "React useEffect Hook",
        "question": "Explain how React's useEffect hook can be used to perform side effects in functional components. Provide an example where useEffect is used to fetch data from an API.",
        "marks": "10"
    },
    {
        "no": 27,
        "topic": "Redux State Management",
        "question": "Describe how to manage state in a React application using Redux. Include an example to illustrate state management in a complex application.",
        "marks": "10"
    },
    {
        "no": 28,
        "topic": "React Features",
        "question": "What is React.js? Discuss different features and advantages of React.js. Why is React popular for modern web development?",
        "marks": "05"
    },
    {
        "no": 29,
        "topic": "RESTful API",
        "question": "What are the criteria for an API to be a RESTful API? Describe how REST APIs function in web development.",
        "marks": "05"
    },
    {
        "no": 30,
        "topic": "Complex Form Validation",
        "question": "Write code to process an online form (Alumni/Signup) with validations: all fields must be filled, valid email (@ and .), age validation (18-60 or DOB >=22 years), username alphanumeric (5-15 characters).",
        "marks": "10"
    }
]

# Print the important questions
print("=" * 100)
print("TOP 30 MOST IMPORTANT QUESTIONS FOR WEB COMPUTING")
print("=" * 100)
print()

for q in important_questions:
    print(f"{q['no']:2d}. [{q['marks']} Marks] {q['topic']}")
    print(f"    Question: {q['question']}")
    print()

print("=" * 100)
