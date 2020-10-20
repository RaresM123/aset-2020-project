Text classification is the problem of constructing models which can classify new texts into pre-defined classes. It involves not only the training of models but also data pre-processing, transformation, and dimensionality reduction.

Text classification speciality literature usually gives off plenty of information about the core elements, techniques, solutions and also future directions of work, proposing the further development of this research area. With that in mind, existing reviews are still useful to this day as the problems addressed are universally available in this field of text classsification (Aas, Eikvil, 1999 [1], Aggarwal, Zhai, 2012 [2]). Although relevant, these researches do not include the latest advancements done in this field. Furthermore, the proposed techniques and algorithms fall mostly under machine learning, omitting other essential elements of text classification, or put accent on a particular research domain (Adeva, Atxa, Carrillo, Zengotitabengoa, 2014 [3], Guzella, Caminhas, 2009 [4], Ittoo, Nguyen, van den Bosch, 2016 [5]). 

We have found more relevant work in the discussed field, which offers a more up to date overview of the current state of text classification:

Feature construction : https://arxiv.org/pdf/1803.11175.pdf
Classification method/Learning methods : https://arxiv.org/pdf/1805.08751.pdf, https://bit.ly/3jij9tH
General overview : https://www.insticc.org/Primoris/Resources/PaperPdf.ashx?idPaper=71885

Google’s Universal Sentence Encoder encodes text into high dimensional vectors that can be used for text classification, semantic similarity, clustering, and other natural language tasks. According to them, the obtained embedding vectors are optimized for transfer learning. Transfer learning is a research problem in machine learning that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem. For example, knowledge gained while learning to recognize cars could apply when trying to recognize trucks. (Wikipedia)
Recurrent neural networks are known to work particularly well with text classification tasks, due to the nature of the input data. The shortcomings of  basic RNNs have been gradually overcome by more advanced architectures, such as LSTM (Long Short-Term Memory) neural networks. LSTMs have been steadily advancing ever since their proposal in 1995.
FAKEDETECTOR, a novel automatic fake news credibility model, introduces plenty of advancements to fake news detection, building an architecturally advanced graph neural network (GNN). Extensive experiments have been done on a real-world fake news dataset to compare FAKEDETECTOR with several state-of-the-art models, and the experimental results have demonstrated the effectiveness of the proposed model.
There are different methods to evaluate a machine learning model. In our project we will use the following metrics to check the performance of our model.
Initially, we will use a confusion matrix to check the number of correctly classified tweets. Afterwards, we will check the accuracy of our model, the precision and recall. We will also use f-recall, the harmonic mean between the precision and the recall. This method is used to show the impact of each metric, so it is the most relevant for overall performance.

Resources and tools: keras, scikit-learn, tweepy and python-twitter, selenium 

Bibliography:
[1] https://d1wqtxts1xzle7.cloudfront.net/30469791/aas99text.pdf?1358890133=&response-content-disposition=inline%3B+filename%3DText_categorisation_A_survey.pdf&Expires=1603226893&Signature=cUKRpE4VKiIC~fmFhhEY9-vc8ufe4ThKnXAnNHvAasNgYQ5AvBKMZwnv2THf3tWrc1bSED4pV1ggG0bMTiWY~O4Xn~kF0g5X1DkMHxy0TJSv0kTWBNjPJ9KP34Qp6vYUqc~2h~PbPZ6BeWtU21SVvcPK9FfahTClnrc62MpWfAXit7xIQJ3M1hPQaiRBN6oZ-~8gGmEdE61UyRBReKdrG6rmJ9FEhUmTYv8jys6wbIJiVhQg12T0hdvTYbqHaUiWQRhpMmG0lW~j8DjWcdb5RMlN4Oea7njyqou09CKyesuZMgSvYiWlEBPvDvlj4cI7BUTKjpBYA8Dp5ihEy4snzg__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
[2] https://link.springer.com/chapter/10.1007/978-1-4614-3223-4_6
[3] https://www.sciencedirect.com/science/article/pii/S0957417413006684
[4] https://www.sciencedirect.com/science/article/pii/S095741740900181X
[5] https://www.sciencedirect.com/science/article/abs/pii/S0166361515300646