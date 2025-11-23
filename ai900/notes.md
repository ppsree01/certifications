# Glossary:

- Transformer model = encoder + decoder
- Encoder = creates embeddings using attention => feeds result of attention to fully connected neural network - to find the best vector representation of embedding
- Attention = examine each token, and determine how it is influenced by the tokens around it
- Decoder = uses embeddings calculated by encoder to determine next most probable token in a sequence started by a prompt. Decoder uses attention + feed forward neural network
- Prompt = input you give to LLM to get a response. Model responds to a prompt with a completion
- System prompts set the behavior and tone of the model and any constraints it should adhere to
- RAG - Retrieval Augmented generation - retrieve info like docs, emails and use it to augment the prompt with relevant data. Response from model is then grounded in the info provided.
- Better prompts:
    - be clear and specific
    - add context
    - use examples
    - ask for structure

- Computer vision = enables AI apps to process visual info
- Contextual image analysis - find contextual relation between objects in images and text that describe them
- Filters - one or more arrays of pixel values called filter kernels. 
- Convolutional Filtering - 
- epochs - one complete pass of complete training data set
- Vision transformer model = model trained with large volumne of images and generates a linear vector from pixel values
- diffusion - a prompt is used to identify a set of related visual features that can be combined to create an image 
- bounding box - abstract rectangle that surrounds text elements in a document
- Face verification - one to one
- Face Identification - one to many

- Azure Vision image analysis - extract insights from images, 
- Azure Content Understanding - extract insights from structured docs, images, audio, video
- Azure Document Intelligence - extract field from digital forms, invoices, reciepts, purchase order, 
- Azure AI search - 
Data capture: Intelligently scanning images to capture and store data values. For example, using a cellphone camera to extract contact information from a business card.
Business process automation: Reading data from forms and using it to trigger workflows. For example, extracting cost center and billing information from invoices and routing them to the appropriate accounts-payable department for processing.
Meeting summarization and analysis: Analyzing and summarizing key points from recorded phone conversations or video conference calls. For example, automating note-taking and action assignments for a team meeting.
Digital asset management (DAM): Managing digital assets like images or videos by automatically tagging and indexing them. For example, to create a searchable library of stock photographs.
Knowledge Mining: Extracting key information from structured and unstructured data to be used for further analysis and reporting. For example, compiling census data from scanned records to populate a database.