# Fashion-Recommendation

## Overview
Fashion Valley is a Streamlit-based web application designed to provide fashion recommendations. Leveraging cosine similarity and the KNN algorithm, it clusters similar types of apparel using image embeddings generated through Convolutional Filters of VGG-16.

## Features
- **Natural Language Processing (NLP) Based Image Search**: Utilizes NLTK for token generation to facilitate image search based on textual descriptions.
- **Display Similar Images**: Displays images similar to a given input image, aiding users in exploring visually similar fashion items.
- **User Purchase History-Based Recommendation**: Offers personalized recommendations based on user purchase history.
- **Gemini API Integration**: Utilizes the Gemini API to suggest complete outfits based on a single piece of apparel, covering topwear, bottomwear, accessories, and more.

![Screenshot 2024-04-28 090817](https://github.com/AkhilVaidya91/Fashion-Recomendation/assets/67970977/0db08775-7115-47fc-b8b4-58702c5d530a)
![Screenshot 2024-04-28 090837](https://github.com/AkhilVaidya91/Fashion-Recomendation/assets/67970977/1cd4e0e4-162d-411b-968a-0716ee07ae3d)
![Screenshot 2024-04-28 091103](https://github.com/AkhilVaidya91/Fashion-Recomendation/assets/67970977/9688b7f6-a80d-46b7-a364-817787961606)

## Machine Learning Models
- **VGG16 Transfer Learning**: Used for generating embeddings from images, providing a rich representation of fashion items.
- **KNN Algorithm**: Implements K-nearest neighbors for clustering similar items based on image embeddings.
- **NLTK**: Employed for natural language processing tasks such as tokenization for enhanced search capabilities.
