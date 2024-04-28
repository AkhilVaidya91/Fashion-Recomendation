# Fashion-Recommendation

## Overview
Fashion Valley is a Streamlit-based web application designed to provide fashion recommendations. Leveraging cosine similarity and the KNN algorithm, it clusters similar types of apparel using image embeddings generated through Convolutional Filters of VGG-16.

## Features
- **Natural Language Processing (NLP) Based Image Search**: Utilizes NLTK for token generation to facilitate image search based on textual descriptions.
- **Display Similar Images**: Displays images similar to a given input image, aiding users in exploring visually similar fashion items.
- **User Purchase History-Based Recommendation**: Offers personalized recommendations based on user purchase history.
- **Gemini API Integration**: Utilizes the Gemini API to suggest complete outfits based on a single piece of apparel, covering topwear, bottomwear, accessories, and more.

## Machine Learning Models
- **VGG16 Transfer Learning**: Used for generating embeddings from images, providing a rich representation of fashion items.
- **KNN Algorithm**: Implements K-nearest neighbors for clustering similar items based on image embeddings.
- **NLTK**: Employed for natural language processing tasks such as tokenization for enhanced search capabilities.
