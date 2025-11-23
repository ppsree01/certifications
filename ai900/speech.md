# Speech Recognition:

- text-tp-speech:
    - capturing audio, preparing features, modelling accoustic patterns, applying language rules, decoding the most likey words, and refining the final output.

PreProcessing:
- MFCC:
    - most common feature extraction technique in speech recognition
    - mimics how human ear percieves sound by emphasising freq where speech energy concentrates and compressing less important ranges

    - How is works:
        - Divide audio into frames
        - Apply fourier transform - convert from time domain to freq domain - revealing which pitches are present
        - Map to Mel scale - adjust freq bins to match human hearing sensitivity - we distinguish low pitches better than high ones
        - Extract coefficients - comprise a small set of numbers that represent spectral shape of the frame
        - The result is a sequence of feature vectors - that captures what the audio sounds like without storing every sample.
        - 13 MFCC feature coefficient

- Accoustic Modeling:
    - learn the relationship between audio features and phonemes - the smallest unit of sound that distinguish words. English uses 44 phonemes
    - accoustic models use transformer architecture - a type of deep neural network 
    - how transformer acheives phoneme prediction:
        - Attention Mechanism - look at surrounding frames to resolve ambiguity
        - Parallel processing - 
        - Contextualised predictions - 

    - The output of acoustic modelling is a probability distribution over phonemes for each audio frame

Language Modelling: 
- Accoustic modeling can confuse words that sound the same, Language models resolve ambiguity by knowledge of vocabulary, grammar, and common word patterns.
- Language models resolve ambiguity by applying knowledge of vocabulary, grammar, and common word patterns
- Some ways in which model guides word sequence prediction:
    - Statistical patterns
    - Contextual awareness
    - Domain adaptation

Decoding:
- Decoding algorithms searchthrough millions of possible word sequences to find the transcription that best matches both accoustic and language model predictions.
    - Beam search decoding:
        - maintains a short list of top-scoring partial transcriptions as it processes each audio frame
        - at each step, it extends the hypothesis with the nxt most likely word, prunes low scoring paths, and keeps only the best candidates

Post processing:
- involves applying formatting rules and corrections to improve readability and accuracy

Pipeline;
- Audio capture
- Preprocessing - MFCC feature that highlight speech pattern
- Accousting modeling
- Language modeling
- Decoding
- Post processing
