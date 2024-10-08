# JCDL 2024 triage approaches

## Dependencies
- pandas 2.2.2  
- numpy 1.26.4  
- openpyxl 3.1.5  
- scikit-learn 1.5.1  
- keras 3.6.0  
- tensorflow 2.17.0  

## Glossaries
sentence-level citation context: the sentence containing the citation marker. For example, from this paragraph from [https://pubs.acs.org/doi/10.1021/acs.joc.9b03129]

From the paragraph: "Nuclear magnetic resonance (NMR) spectroscopy is one of the pivotal analytical tools used to determine key chemical properties of organic compounds, for example, relative/ absolute configurations,1,2 and to provide further structural information, for example, representative conformational patterns of the investigated molecules.3 In this context, the spectroscopic properties of organic compounds can be proficiently predicted by accurate quantum chemical meth- ods.1,4−7 Indeed, the integration of the information from experimental and computational data can then be of fundamental importance to solve different structural issues of organic compounds. In the last decade, different studies were performed with the combination of the information from NMR spectroscopy (experimental part) and quantum mechanical (QM) calculations (predicted part) (QM/NMR integrated approach) for the successful elucidation of the configurational patterns of organic compounds.1,4 Also, this approach is helpful for the stereostructural assignment of natural compounds, thus representing a reliable alternative, faster and cheaper, to total synthesis.8 Also, the notable advances in computer science nowadays allows the perform- ance of accurate conformational sampling and QM calculations even on desktop computers, thus facilitating the structural elucidation process."

There are TWO sentence-level citation context for citation marker **1** discovered from this paragraph: 


"Nuclear magnetic resonance (NMR) spectroscopy is one of the pivotal analytical tools used to determine key chemical properties of organic compounds, for example, relative/ absolute configurations,1,2 and to provide further structural information, for example, representative conformational patterns of the investigated molecules.3 In this context, the spectroscopic properties of organic compounds can be proficiently predicted by accurate quantum chemical meth- ods.1,4−7"


and


"In the last decade, different studies were performed with the combination of the information from NMR spectroscopy (experimental part) and quantum mechanical (QM) calculations (predicted part) (QM/NMR integrated approach) for the successful elucidation of the configurational patterns of organic compounds.1,4 "


## File Structure and Explanations
### LSTM.ipynb
An LSTM model to predict the whether a sentence-level citation context indicates risk of the citing publication propagate unreliability (Y or N)
Code adapted from: https://github.com/Conferences2023/TPDL/blob/main/Citation%20Analysis/LSTM.py

'code of Usman, M., & Balke, W.-T. (2023). On retraction cascade? Citation intention analysis as a quality control mechanism in digital libraries. In O. Alonso, H. Cousijn, G. Silvello, M. Marrero, C. Teixeira Lopes, & S. Marchesin (Eds.), Linking Theory and Practice of Digital Libraries (pp. 117–131). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-43849-3_11'

Input: ML_input_data
- all_data.csv: all citation context sentences
- train_set.csv: the train set
- test_set.csv: the test set
  
Output: ML_output_data
- LSTM_prediction_203.csv: predictions for all sentence-level citation contexts: Y or N

### decision_tree.ipynb

Code for the three approaches: the base approach, the keyword-based approach (Approach-KW), and the machine learning-based approach (Approach-ML)

Input:
- input_data/keyword_dictionary.csv: all keywords used in the keywords approach
- input_data/LSTM_prediction_203.csv: the prediction of the citing publication propagating risks of the publication from the LSTM model, only for the sentence-level citation context from 203 publications going into stage 3
- input_data/metadata.csv: metadata needed for the decision trees
- input_data/citation_context_sentence.csv: the sentence-level citation context (for decision tree as well, the keyword approach)

Output:
- decision_tree_output_data/decision_df_keywords.csv: decisions made by the keyword approach (Approch-KW)
- decision_tree_output_data/decision_df_ml.csv: decisions made by the machine learning-based approach (Approach-ML)

### evaluation.ipynb
Input:
- decision_tree_output/decision_df_keywords.csv: decisions made by the keyword approach (Approch-KW)
- decision_tree_output/decision_df_ml.csv: decisions made by the machine learning-based approach (Approach-ML)
- input_data/pub_annotation.csv: silver standard annotation

Output:
- eval_keyword_silver: comparison between the keyword-based approach and the silver standard
- eval_ml_silver: comparison between the machine learning-based approach and the silver standard
- performance_metrics.tsv: perfomrnace metrics of the three approaches, correponding to Table 3 of the publication






