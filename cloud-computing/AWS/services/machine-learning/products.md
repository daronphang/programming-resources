## Amazon CodeGuru

An ML-powered service for automated code reviews and application performance recommendations. Provides two functionalities:

- Reviewer: Automated code reviews for static code analysis
- Profiler: Visibility/recommendations about application performances during runtime (production)

## Amazon Sagemaker

Amazon Sagemaker is a cloud-based machine-learning platform that allows users to construct, design, train, tune, and deploy **machine-learning models** in a production-ready hosted environment (fully managed infrastructure, tools, and workflows):

- Building
- Labeling
- Training

To enable inter-container traffic encryption, set EnableInterContainerTrafficEncryption parameter to true when creating training jobs.

### Workflow

1. Data ingestion
2. Data preparation and exploration
3. Model training
4. Model evaluation and tuning
5. Model deployment

### Features

- Built-in algorithms and BYOA
- Integrated Jupyter notebooks
- Distributed training
- Automatic model tuning
- SageMaker Studio IDE

## Amazon Augmented AI (A2I)

Amazon Augmented AI provides built-in human review workflows for common machine learning use cases, such as content moderation and text extraction from documents.

With Amazon A2I, a person can also create their own workflows for machine learning models built on Amazon SageMaker or any other tools.

### Features

- Built-in human review workflows (second opinion about ML data to improve the confidence of that labeled data)
- Access to human reviewers
- Continuous learning and improvement
- Seamless scaling

## Amazon Textract

Amazon Textract is a machine learning service that automatically extracts text and data from scanned documents.

## Amazon Polly

Amazon Polly is a machine learning service that converts text to speech. This service provides the ability to read text out loud.

### Features

- Lifelike speech
- Real-time streaming or file generation
- Speech-Synthesis ML (SSML) support
- Lexicon support

## Amazon Transcribe

Automatically converts speech to text using a deep learning process called automatic speech recognition (ASR). Supports Automatic Language Identification for multi-lingual audio.

### Features

- Automatic speech recognition
- Real-time transcription
- Custom vocabulary
- Speaker identification (up to 10 speakers)

## Amazon Lex

Provides ASR to convert speech to text (using same technology that powers Alexa). Helps build chatbots and call center bots.

### Features

- Natural Language Understanding (NLU) to recognize the intention of the text
- Automatic Speech Recognition (ASR) to interpret the user inputs and convert speech to text
- Easy to build
- Fully managed
- Multi-channel support e.g. mobile, IoT,

## Amazon Connect

Cloud-based virtual contact center to receive calls and create contact flows. Can integrate with other Customer Relations Management (CRM) systems or AWS.

## Amazon Rekognition

Find objects, people, text, scenes in images and videos using ML. Able to perform facial analysis and facial search to do user verification, people counting, etc. Provides suggested keywords and tags the image.

Rekognition can be used for **content moderation**, which is the process of monitoring the viewing and managing user-generated content to meet the established guidelines and standards.

### Features

- Object and scene detection
- Facial analysis and recognition
- Text in image
- Activity detection
- Unsafe content detection
- Celebrity recognition
- Custom labels
- Emotion detection
- Real-time analysis

## Amazon Translate

Provides natural and accurate language translation.

```
Source text stored in S3 -> Triggers Lambda -> Calls Translate -> Output text to S3
```

### Features

- Neural machine translation to provide more accuracy
- Wide range of supported languages (over 5,000)
- Real-time translation
- Seamless integration
- Custom terminology

## Amazon Comprehend

Amazon Comprehend is a text analysis machine; it will derive meaningful insights about the data you give it. It is a fully managed and serverless service used for Natural Language Processing (NLP). Uses ML to find insights and relationships in text including:

- Language of the text
- Extracting key phrases, places, people, brands, or events
- Understanding how positive/negative the text is

```
S3 -> AWS Lambda -> Amazon Comprehend -> Store in S3
```

### Features

- Language detection
- Sentiment analysis
- Entity recognition
- Key phrases extraction
- Topic modeling
- Syntax analysis
- PII detection and removal (personal identifiable identity)
- Multilingual support
- Real-time processing

## Amazon Forecast

Fully managed service that uses ML to deliver highly accurate forecasts. It is used to take time-series data to tell you the probability of something happening and based on historical patterns and analysis.

It can do predictions by automating the complex steps involved, and doesn't require prior ML experience like SageMaker.

### Features

- Fully managed
- Easy to use
- Accurate forecasts
- Quantiles

## Amazon Kendra

Fully managed document search service powered by ML. Extracts answers from within a document i.e. PDF, text, HTML, Powerpoint, MSWord, etc.

## Amazon Personalize

Fully managed ML-service to build apps with real-time personalized recommendations based on user behavior i.e. what users search/buy. Uses the same technology used by Amazon.com.

## AWS Fraud Detector

A fully-managed service used to identify potential fraudulent activities more effectively without any prior ML experience.

### Workflow

1. Define business-use case
2. Input historical data
3. Select model type and train model
4. Generate model scores and evaluate performance
5. Adjust and retrain model
6. Establish decision logic
7. Create and deploy detector
8. Real-time or batch fraud evaluation
9. Assign outcomes and take action
10. Feedback and continuous improvement

### Features

- Real-time fraud detection
- Pre-built and customizable detectors
- Built-in data encryption and access management
