from dataclasses import dataclass
from typing import Optional, List

@dataclass
class DatasetEntry:
    dataset: str
    dataset_key: str
    citation_key: str
    citation: str
    anthology: Optional[str]
    languages: List[str]
    license: str

DATASETS: List[DatasetEntry] = [
    DatasetEntry(
        dataset='CaLMQA',
        dataset_key='shanearora/CaLMQA',
        citation_key='arora2024calmqa',
        citation='@misc{arora2024calmqa,\n      title={CaLMQA: Exploring culturally specific long-form question answering across 23 languages}, \n      author={Shane Arora and Marzena Karpinska and Hung-Ting Chen and Ipsita Bhattacharjee and Mohit Iyyer and Eunsol Choi},\n      year={2024},\n      eprint={2406.17761},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2406.17761}, \n}',
        anthology=None,
        languages=['EN', 'KO'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='BLEnD',
        dataset_key='nayeon212/BLEnD',
        citation_key='myung2024blend',
        citation='@misc{myung2025blend,\n      title={BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages}, \n      author={Junho Myung and Nayeon Lee and Yi Zhou and Jiho Jin and Rifki Afina Putri and Dimosthenis Antypas and Hsuvas Borkakoty and Eunsu Kim and Carla Perez-Almendros and Abinew Ali Ayele and Víctor Gutiérrez-Basulto and Yazmín Ibáñez-García and Hwaran Lee and Shamsuddeen Hassan Muhammad and Kiwoong Park and Anar Sabuhi Rzayev and Nina White and Seid Muhie Yimam and Mohammad Taher Pilehvar and Nedjma Ousidhoum and Jose Camacho-Collados and Alice Oh},\n      year={2025},\n      eprint={2406.09948},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2406.09948}, \n}',
        anthology=None,
        languages=['KO'],
        license='cc-by-sa-4.0'
    ),
    DatasetEntry(
        dataset='KBL',
        dataset_key='lbox/kbl',
        citation_key='kimyeeun-etal-2024-developing',
        citation='@inproceedings{kimyeeun-etal-2024-developing,\n    title = "Developing a Pragmatic Benchmark for Assessing {K}orean Legal Language Understanding in Large Language Models",\n    author = "Kim, Yeeun  and\n      Choi, Youngrok  and\n      Choi, Eunkyung  and\n      Choi, JinHwan  and\n      Park, Hai Jin  and\n      Hwang, Wonseok",\n    editor = "Al-Onaizan, Yaser  and\n      Bansal, Mohit  and\n      Chen, Yun-Nung",\n    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",\n    month = nov,\n    year = "2024",\n    address = "Miami, Florida, USA",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2024.findings-emnlp.319/",\n    doi = "10.18653/v1/2024.findings-emnlp.319",\n    pages = "5573--5595",\n    abstract = "Large language models (LLMs) have demonstrated remarkable performance in the legal domain, with GPT-4 even passing the Uniform Bar Exam in the U.S. However their efficacy remains liMITed for non-standardized tasks and tasks in languages other than English. This underscores the need for careful evaluation of LLMs within each legal system before application.Here, we introduce KBL, a benchmark for assessing the Korean legal language understanding of LLMs, consisting of (1) 7 legal knowledge tasks (510 examples), (2) 4 legal reasoning tasks (288 examples), and (3) the Korean bar exam (4 domains, 53 tasks, 2,510 examples). First two datasets were developed in close collaboration with lawyers to evaluate LLMs in practical scenarios in a certified manner. Furthermore, considering legal practitioners\' frequent use of extensive legal documents for research, we assess LLMs in both a closed book setting, where they rely solely on internal knowledge, and a retrieval-augmented generation (RAG) setting, using a corpus of Korean statutes and precedents. The results indicate substantial room and opportunities for improvement."\n}',
        anthology='kimyeeun-etal-2024-developing',
        languages=['KO'],
        license='cc-by-nc-4.0'
    ),
    DatasetEntry(
        dataset='KorMedMCQA',
        dataset_key='sean0042/KorMedMCQA',
        citation_key='kweon2024kormedmcqa',
        citation='@misc{kweon2024kormedmcqa,\n      title={KorMedMCQA: Multi-Choice Question Answering Benchmark for Korean Healthcare Professional Licensing Examinations}, \n      author={Sunjun Kweon and Byungjin Choi and Gyouk Chu and Junyeong Song and Daeun Hyeon and Sujin Gan and Jueon Kim and Minkyu Kim and Rae Woong Park and Edward Choi},\n      year={2024},\n      eprint={2403.01469},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2403.01469}, \n}',
        anthology=None,
        languages=['KO'],
        license='cc-by-nc-2.0'
    ),
    DatasetEntry(
        dataset='KMMLU',
        dataset_key='HAERAE-HUB/KMMLU',
        citation_key='son-etal-2025-kmmlu',
        citation='@inproceedings{son-etal-2025-kmmlu,\n    title = "{KMMLU}: Measuring Massive Multitask Language Understanding in {K}orean",\n    author = "Son, Guijin  and\n      Lee, Hanwool  and\n      Kim, Sungdong  and\n      Kim, Seungone  and\n      Muennighoff, Niklas  and\n      Choi, Taekyoon  and\n      Park, Cheonbok  and\n      Yoo, Kang Min  and\n      Biderman, Stella",\n    editor = "Chiruzzo, Luis  and\n      Ritter, Alan  and\n      Wang, Lu",\n    booktitle = "Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",\n    month = apr,\n    year = "2025",\n    address = "Albuquerque, New Mexico",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2025.naacl-long.206/",\n    pages = "4076--4104",\n    ISBN = "979-8-89176-189-6",\n    abstract = "We propose KMMLU, a Korean benchmark with 35,030 expert-level multiple-choice questions across 45 subjects ranging from humanities to STEM. While prior Korean evaluation tools heavily rely on translated versions of existing English benchmarks, KMMLU is collected from original Korean exams, thereby capturing linguistic and cultural aspects of the Korean language. Recent models struggle to show performance over 60{\\%}, significantly below the pass mark of the source exams (80{\\%}), highlighting the room for improvement. Notably, one-fifth of the questions in KMMLU require knowledge of Korean culture for accurate resolution. KMMLU thus provides a more accurate reflection of human preferences compared to translated versions of MMLU and offers deeper insights into LLMs\' shortcomings in Korean knowledge. The dataset and codes are made publicly available for future research."\n}',
        anthology='son-etal-2025-kmmlu',
        languages=['KO'],
        license='cc-by-nd-4.0'
    ),
    DatasetEntry(
        dataset='HRM8K',
        dataset_key='HAERAE-HUB/HRM8K',
        citation_key='ko2025understand',
        citation='@misc{ko2025understand,\n      title={Understand, Solve and Translate: Bridging the Multilingual Mathematical Reasoning Gap}, \n      author={Hyunwoo Ko and Guijin Son and Dasol Choi},\n      year={2025},\n      eprint={2501.02448},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2501.02448}, \n}',
        anthology=None,
        languages=['KO'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='KoBBQ',
        dataset_key='naver-ai/kobbq',
        citation_key='jin-etal-2024-kobbq',
        citation='@article{jin-etal-2024-kobbq,\n    title = "{K}o{BBQ}: {K}orean Bias Benchmark for Question Answering",\n    author = "Jin, Jiho  and\n      Kim, Jiseon  and\n      Lee, Nayeon  and\n      Yoo, Haneul  and\n      Oh, Alice  and\n      Lee, Hwaran",\n    journal = "Transactions of the Association for Computational Linguistics",\n    volume = "12",\n    year = "2024",\n    address = "Cambridge, MA",\n    publisher = "MIT Press",\n    url = "https://aclanthology.org/2024.tacl-1.28/",\n    doi = "10.1162/tacl_a_00661",\n    pages = "507--524",\n    abstract = "Warning: This paper contains examples of stereotypes and biases. The Bias Benchmark for Question Answering (BBQ) is designed to evaluate social biases of language models (LMs), but it is not simple to adapt this benchmark to cultural contexts other than the US because social biases depend heavily on the cultural context. In this paper, we present KoBBQ, a Korean bias benchmark dataset, and we propose a general framework that addresses considerations for cultural adaptation of a dataset. Our framework includes partitioning the BBQ dataset into three classes{---}Simply-Transferred (can be used directly after cultural translation), Target-Modified (requires localization in target groups), and Sample-Removed (does not fit Korean culture){---}and adding four new categories of bias specific to Korean culture. We conduct a large-scale survey to collect and validate the social biases and the targets of the biases that reflect the stereotypes in Korean culture. The resulting KoBBQ dataset comprises 268 templates and 76,048 samples across 12 categories of social bias. We use KoBBQ to measure the accuracy and bias scores of several state-of-the-art multilingual LMs. The results clearly show differences in the bias of LMs as measured by KoBBQ and a machine-translated version of BBQ, demonstrating the need for and utility of a well-constructed, culturally aware social bias benchmark."\n}',
        anthology='jin-etal-2024-kobbq',
        languages=['KO'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='KULTURE Bench',
        dataset_key='KULTUREBench',
        citation_key='wang2024kulture',
        citation='@misc{wang2024kulture,\n      title={KULTURE Bench: A Benchmark for Assessing Language Model in Korean Cultural Context}, \n      author={Xiaonan Wang and Jinyoung Yeo and Joon-Ho Lim and Hansaem Kim},\n      year={2024},\n      eprint={2412.07251},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2412.07251}, \n}',
        anthology=None,
        languages=['KO'],
        license=' Apache-2.0'
    ),
    DatasetEntry(
        dataset='HAE-RAE Bench',
        dataset_key='HAERAE-HUB/HAE_RAE_BENCH_1.1',
        citation_key='son-etal-2024-hae',
        citation='@inproceedings{son-etal-2024-hae,\n    title = "{HAE}-{RAE} Bench: Evaluation of {K}orean Knowledge in Language Models",\n    author = "Son, Guijin  and\n      Lee, Hanwool  and\n      Kim, Suwan  and\n      Kim, Huiseo  and\n      Lee, Jae cheol  and\n      Yeom, Je Won  and\n      Jung, Jihyu  and\n      Kim, Jung woo  and\n      Kim, Songseong",\n    editor = "Calzolari, Nicoletta  and\n      Kan, Min-Yen  and\n      Hoste, Veronique  and\n      Lenci, Alessandro  and\n      Sakti, Sakriani  and\n      Xue, Nianwen",\n    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",\n    month = may,\n    year = "2024",\n    address = "Torino, Italia",\n    publisher = "ELRA and ICCL",\n    url = "https://aclanthology.org/2024.lrec-main.704/",\n    pages = "7993--8007",\n    abstract = "Large language models (LLMs) trained on massive corpora demonstrate impressive capabilities in a wide range of tasks. While there are ongoing efforts to adapt these models to languages beyond English, the attention given to their evaluation methodologies remains liMITed. Current multilingual benchmarks often rely on back translations or re-implementations of English tests, liMITing their capacity to capture unique cultural and linguistic nuances. To bridge this gap for the Korean language, we introduce the HAE-RAE Bench, a dataset curated to challenge models lacking Korean cultural and contextual depth. The dataset encompasses six downstream tasks across four domains: vocabulary, history, general knowledge, and reading comprehension. Unlike traditional evaluation suites focused on token and sequence classification or mathematical and logical reasoning, the HAE-RAE Bench emphasizes a model{\'}s aptitude for recalling Korean-specific knowledge and cultural contexts. Comparative analysis with prior Korean benchmarks indicates that the HAE-RAE Bench presents a greater challenge to non-Korean models by disturbing abilities and knowledge learned from English being transferred."\n}',
        anthology='son-etal-2024-hae',
        languages=['KO'],
        license='cc-by-nc-nd-4.0'
    ),
    DatasetEntry(
        dataset='CLIcK',
        dataset_key='EunsuKim/CLIcK',
        citation_key='kim-etal-2024-click',
        citation='@inproceedings{kim-etal-2024-click,\n    title = "{CLI}c{K}: A Benchmark Dataset of Cultural and Linguistic Intelligence in {K}orean",\n    author = "Kim, Eunsu  and\n      Suk, Juyoung  and\n      Oh, Philhoon  and\n      Yoo, Haneul  and\n      Thorne, James  and\n      Oh, Alice",\n    editor = "Calzolari, Nicoletta  and\n      Kan, Min-Yen  and\n      Hoste, Veronique  and\n      Lenci, Alessandro  and\n      Sakti, Sakriani  and\n      Xue, Nianwen",\n    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",\n    month = may,\n    year = "2024",\n    address = "Torino, Italia",\n    publisher = "ELRA and ICCL",\n    url = "https://aclanthology.org/2024.lrec-main.296/",\n    pages = "3335--3346",\n    abstract = "Despite the rapid development of large language models (LLMs) for the Korean language, there remains an obvious lack of benchmark datasets that test the requisite Korean cultural and linguistic knowledge. Because many existing Korean benchmark datasets are derived from the English counterparts through translation, they often overlook the different cultural contexts. For the few benchmark datasets that are sourced from Korean data capturing cultural knowledge, only narrow tasks such as hate speech detection are offered. To address this gap, we introduce a benchmark of Cultural and Linguistic Intelligence in Korean (CLIcK), a dataset comprising 1,995 QA pairs. CLIcK sources its data from official Korean exams and textbooks, partitioning the questions into eleven categories under the two main categories of language and culture. For each instance in click, we provide fine-grained annotation of which cultural and linguistic knowledge is required to correctly answer the question. Using CLIcK, we test 13 language models to assess their performance. Our evaluation uncovers insights into their performances across the categories, as well as the diverse factors affecting their comprehension. CLIcK offers the first large-scale comprehensive Korean-centric analysis of LLMs\' proficiency in Korean language and culture."\n}',
        anthology='kim-etal-2024-click',
        languages=['KO'],
        license='cc-by-nd-4.0'
    ),
    DatasetEntry(
        dataset='HRMCR',
        dataset_key='HAERAE-HUB/HRMCR',
        citation_key='son-etal-2025-multi',
        citation='@inproceedings{son-etal-2025-multi,\n    title = "Multi-Step Reasoning in {K}orean and the Emergent Mirage",\n    author = "Son, Guijin  and\n      Ko, Hyunwoo  and\n      Choi, Dasol",\n    editor = "Prabhakaran, Vinodkumar  and\n      Dev, Sunipa  and\n      Benotti, Luciana  and\n      Hershcovich, Daniel  and\n      Cao, Yong  and\n      Zhou, Li  and\n      Cabello, Laura  and\n      Adebara, Ife",\n    booktitle = "Proceedings of the 3rd Workshop on Cross-Cultural Considerations in NLP (C3NLP 2025)",\n    month = may,\n    year = "2025",\n    address = "Albuquerque, New Mexico",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2025.c3nlp-1.2/",\n    pages = "10--21",\n    ISBN = "979-8-89176-237-4"\n}',
        anthology='son-etal-2025-multi',
        languages=['KO'],
        license='apache-2.0'
    ),
    DatasetEntry(
        dataset='KoSBi',
        dataset_key='nayohan/KoSBi',
        citation_key='lee-etal-2023-kosbi',
        citation='@inproceedings{lee-etal-2023-kosbi,\n    title = "{K}o{SBI}: A Dataset for MITigating Social Bias Risks Towards Safer Large Language Model Applications",\n    author = "Lee, Hwaran  and\n      Hong, Seokhee  and\n      Park, Joonsuk  and\n      Kim, Takyoung  and\n      Kim, Gunhee  and\n      Ha, Jung-woo",\n    editor = "Sitaram, Sunayana  and\n      Beigman Klebanov, Beata  and\n      Williams, Jason D",\n    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 5: Industry Track)",\n    month = jul,\n    year = "2023",\n    address = "Toronto, Canada",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2023.acl-industry.21/",\n    doi = "10.18653/v1/2023.acl-industry.21",\n    pages = "208--224",\n    abstract = "Large language models (LLMs) not only learn natural text generation abilities but also social biases against different demographic groups from real-world data. This poses a critical risk when deploying LLM-based applications. Existing research and resources are not readily applicable in South Korea due to the differences in language and culture, both of which significantly affect the biases and targeted demographic groups. This liMITation requires localized social bias datasets to ensure the safe and effective deployment of LLMs. To this end, we present KosBi, a new social bias dataset of 34k pairs of contexts and sentences in Korean covering 72 demographic groups in 15 categories. We find that through filtering-based moderation, social biases in generated content can be reduced by 16.47{\\%}p on average for HyperClova (30B and 82B), and GPT-3."\n}',
        anthology='lee-etal-2023-kosbi',
        languages=['KO'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='ARC',
        dataset_key=None,
        citation_key='allenai:arc',
        citation='@article{allenai:arc,\n      author    = {Peter Clark  and Isaac Cowhey and Oren Etzioni and Tushar Khot and\n                    Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},\n      title     = {Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},\n      journal   = {arXiv:1803.05457v1},\n      year      = {2018},\n}',
        anthology=None,
        languages=['EN'],
        license='CC BY-SA 4.0'
    ),
    DatasetEntry(
        dataset='SocialIQA',
        dataset_key=None,
        citation_key='sap-etal-2019-social',
        citation='@inproceedings{sap-etal-2019-social,\n    title = "Social {IQ}a: Commonsense Reasoning about Social Interactions",\n    author = "Sap, Maarten  and\n      Rashkin, Hannah  and\n      Chen, Derek  and\n      Le Bras, Ronan  and\n      Choi, Yejin",\n    editor = "Inui, Kentaro  and\n      Jiang, Jing  and\n      Ng, Vincent  and\n      Wan, Xiaojun",\n    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",\n    month = nov,\n    year = "2019",\n    address = "Hong Kong, China",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/D19-1454/",\n    doi = "10.18653/v1/D19-1454",\n    pages = "4463--4473",\n    abstract = "We introduce Social IQa, the first large-scale benchmark for commonsense reasoning about social situations. Social IQa contains 38,000 multiple choice questions for probing emotional and social intelligence in a variety of everyday situations (e.g., Q: ``Jordan wanted to tell Tracy a secret, so Jordan leaned towards Tracy. Why did Jordan do this?\'\' A: ``Make sure no one else could hear\'\'). Through crowdsourcing, we collect commonsense questions along with correct and incorrect answers about social interactions, using a new framework that mitigates stylistic artifacts in incorrect answers by asking workers to provide the right answer to a different but related question. Empirical results show that our benchmark is challenging for existing question-answering models based on pretrained language models, compared to human performance ({\\ensuremath{>}}20{\\%} gap). Notably, we further establish Social IQa as a resource for transfer learning of commonsense knowledge, achieving state-of-the-art performance on multiple commonsense reasoning tasks (Winograd Schemas, COPA)."\n}',
        anthology='sap-etal-2019-social',
        languages=['EN'],
        license='CC0'
    ),
    DatasetEntry(
        dataset='TriviaQA',
        dataset_key=None,
        citation_key='joshi-etal-2017-triviaqa',
        citation='@inproceedings{joshi-etal-2017-triviaqa,\n    title = "{T}rivia{QA}: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension",\n    author = "Joshi, Mandar  and\n      Choi, Eunsol  and\n      Weld, Daniel  and\n      Zettlemoyer, Luke",\n    editor = "Barzilay, Regina  and\n      Kan, Min-Yen",\n    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",\n    month = jul,\n    year = "2017",\n    address = "Vancouver, Canada",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/P17-1147/",\n    doi = "10.18653/v1/P17-1147",\n    pages = "1601--1611",\n    abstract = "We present TriviaQA, a challenging reading comprehension dataset containing over 650K question-answer-evidence triples. TriviaQA includes 95K question-answer pairs authored by trivia enthusiasts and independently gathered evidence documents, six per question on average, that provide high quality distant supervision for answering the questions. We show that, in comparison to other recently introduced large-scale datasets, TriviaQA (1) has relatively complex, compositional questions, (2) has considerable syntactic and lexical variability between questions and corresponding answer-evidence sentences, and (3) requires more cross sentence reasoning to find answers. We also present two baseline algorithms: a feature-based classifier and a state-of-the-art neural network, that performs well on SQuAD reading comprehension. Neither approach comes close to human performance (23{\\%} and 40{\\%} vs. 80{\\%}), suggesting that TriviaQA is a challenging testbed that is worth significant future study."\n}',
        anthology='joshi-etal-2017-triviaqa',
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='WinoGrande',
        dataset_key=None,
        citation_key='winogrande2021sakaguchi',
        citation='@article{winogrande2021sakaguchi,\nauthor = {Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},\ntitle = {WinoGrande: an adversarial winograd schema challenge at scale},\nyear = {2021},\nissue_date = {September 2021},\npublisher = {Association for Computing Machinery},\naddress = {New York, NY, USA},\nvolume = {64},\nnumber = {9},\nissn = {0001-0782},\nurl = {https://doi.org/10.1145/3474381},\ndoi = {10.1145/3474381},\nabstract = {Commonsense reasoning remains a major challenge in AI, and yet, recent progresses on benchmarks may seem to suggest otherwise. In particular, the recent neural language models have reported above 90\\% accuracy on the Winograd Schema Challenge (WSC), a commonsense benchmark originally designed to be unsolvable for statistical models that rely simply on word associations. This raises an important question---whether these models have truly acquired robust commonsense capabilities or they rely on spurious biases in the dataset that lead to an overestimation of the true capabilities of machine commonsense.To investigate this question, we introduce WinoGrande, a large-scale dataset of 44k problems, inspired by the original WSC, but adjusted to improve both the scale and the hardness of the dataset. The key steps of the dataset construction consist of (1) large-scale crowdsourcing, followed by (2) systematic bias reduction using a novel AFLITE algorithm that generalizes human-detectable word associations to machine-detectable embedding associations. Our experiments demonstrate that state-of-the-art models achieve considerably lower accuracy (59.4\\%-79.1\\%) on WINOGRANDE compared to humans (94\\%), confirming that the high performance on the original WSC was inflated by spurious biases in the dataset.Furthermore, we report new state-of-the-art results on five related benchmarks with emphasis on their dual implications. On the one hand, they demonstrate the effectiveness of WINOGRANDE when used as a resource for transfer learning. On the other hand, the high performance on all these benchmarks suggests the extent to which spurious biases are prevalent in all such datasets, which motivates further research on algorithmic bias reduction.},\njournal = {Commun. ACM},\nmonth = aug,\npages = {99–106},\nnumpages = {8}\n}',
        anthology=None,
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='Natural Questions (open)',
        dataset_key=None,
        citation_key='kwiatkowski-etal-2019-natural',
        citation='@article{kwiatkowski-etal-2019-natural,\n    title = "Natural Questions: A Benchmark for Question Answering Research",\n    author = "Kwiatkowski, Tom  and\n      Palomaki, Jennimaria  and\n      Redfield, Olivia  and\n      Collins, Michael  and\n      Parikh, Ankur  and\n      Alberti, Chris  and\n      Epstein, Danielle  and\n      Polosukhin, Illia  and\n      Devlin, Jacob  and\n      Lee, Kenton  and\n      Toutanova, Kristina  and\n      Jones, Llion  and\n      Kelcey, Matthew  and\n      Chang, Ming-Wei  and\n      Dai, Andrew M.  and\n      Uszkoreit, Jakob  and\n      Le, Quoc  and\n      Petrov, Slav",\n    editor = "Lee, Lillian  and\n      Johnson, Mark  and\n      Roark, Brian  and\n      Nenkova, Ani",\n    journal = "Transactions of the Association for Computational Linguistics",\n    volume = "7",\n    year = "2019",\n    address = "Cambridge, MA",\n    publisher = "MIT Press",\n    url = "https://aclanthology.org/Q19-1026/",\n    doi = "10.1162/tacl_a_00276",\n    pages = "452--466",\n    abstract = "We present the Natural Questions corpus, a question answering data set. Questions consist of real anonymized, aggregated queries issued to the Google search engine. An annotator is presented with a question along with a Wikipedia page from the top 5 search results, and annotates a long answer (typically a paragraph) and a short answer (one or more entities) if present on the page, or marks null if no long/short answer is present. The public release consists of 307,373 training examples with single annotations; 7,830 examples with 5-way annotations for development data; and a further 7,842 examples with 5-way annotated sequestered as test data. We present experiments validating quality of the data. We also describe analysis of 25-way annotations on 302 examples, giving insights into human variability on the annotation task. We introduce robust metrics for the purposes of evaluating question answering systems; demonstrate high human upper bounds on these metrics; and establish baseline results using competitive methods drawn from related literature."\n}',
        anthology=None,
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='NarrativeQA',
        dataset_key=None,
        citation_key='kocisky-etal-2018-narrativeqa',
        citation='@article{kocisky-etal-2018-narrativeqa,\n    title = "The {N}arrative{QA} Reading Comprehension Challenge",\n    author = "Ko{\\v{c}}isk{\\\'y}, Tom{\\\'a}{\\v{s}}  and\n      Schwarz, Jonathan  and\n      Blunsom, Phil  and\n      Dyer, Chris  and\n      Hermann, Karl Moritz  and\n      Melis, G{\\\'a}bor  and\n      Grefenstette, Edward",\n    editor = "Lee, Lillian  and\n      Johnson, Mark  and\n      Toutanova, Kristina  and\n      Roark, Brian",\n    journal = "Transactions of the Association for Computational Linguistics",\n    volume = "6",\n    year = "2018",\n    address = "Cambridge, MA",\n    publisher = "MIT Press",\n    url = "https://aclanthology.org/Q18-1023/",\n    doi = "10.1162/tacl_a_00023",\n    pages = "317--328",\n    abstract = "Reading comprehension (RC){---}in contrast to information retrieval{---}requires integrating information and reasoning about events, entities, and their relations across a full document. Question answering is conventionally used to assess RC ability, in both artificial agents and children learning to read. However, existing RC datasets and tasks are dominated by questions that can be solved by selecting answers using superficial information (e.g., local context similarity or global term frequency); they thus fail to test for the essential integrative aspect of RC. To encourage progress on deeper comprehension of language, we present a new dataset and set of tasks in which the reader must answer questions about stories by reading entire books or movie scripts. These tasks are designed so that successfully answering their questions requires understanding the underlying narrative rather than relying on shallow pattern matching or salience. We show that although humans solve the tasks easily, standard RC models struggle on the tasks presented here. We provide an analysis of the dataset and the challenges it presents."\n}',
        anthology='kocisky-etal-2018-narrativeqa',
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='TruthfulQA',
        dataset_key=None,
        citation_key='lin-etal-2022-truthfulqa',
        citation='@inproceedings{lin-etal-2022-truthfulqa,\n    title = "{T}ruthful{QA}: Measuring How Models Mimic Human Falsehoods",\n    author = "Lin, Stephanie  and\n      Hilton, Jacob  and\n      Evans, Owain",\n    editor = "Muresan, Smaranda  and\n      Nakov, Preslav  and\n      Villavicencio, Aline",\n    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",\n    month = may,\n    year = "2022",\n    address = "Dublin, Ireland",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2022.acl-long.229/",\n    doi = "10.18653/v1/2022.acl-long.229",\n    pages = "3214--3252",\n    abstract = "We propose a benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts. We tested GPT-3, GPT-Neo/J, GPT-2 and a T5-based model. The best model was truthful on 58{\\%} of questions, while human performance was 94{\\%}. Models generated many false answers that mimic popular misconceptions and have the potential to deceive humans. The largest models were generally the least truthful. This contrasts with other NLP tasks, where performance improves with model size. However, this result is expected if false answers are learned from the training distribution. We suggest that scaling up models alone is less promising for improving truthfulness than fine-tuning using training objectives other than imitation of text from the web."\n}',
        anthology='lin-etal-2022-truthfulqa',
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='Open-BookQA',
        dataset_key=None,
        citation_key='mihaylov-etal-2018-suit',
        citation='@inproceedings{mihaylov-etal-2018-suit,\n    title = "Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering",\n    author = "Mihaylov, Todor  and\n      Clark, Peter  and\n      Khot, Tushar  and\n      Sabharwal, Ashish",\n    editor = "Riloff, Ellen  and\n      Chiang, David  and\n      Hockenmaier, Julia  and\n      Tsujii, Jun{\'}ichi",\n    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",\n    month = oct # "-" # nov,\n    year = "2018",\n    address = "Brussels, Belgium",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/D18-1260/",\n    doi = "10.18653/v1/D18-1260",\n    pages = "2381--2391",\n    abstract = "We present a new kind of question answering dataset, OpenBookQA, modeled after open book exams for assessing human understanding of a subject. The open book that comes with our questions is a set of 1326 elementary level science facts. Roughly 6000 questions probe an understanding of these facts and their application to novel situations. This requires combining an open book fact (e.g., metals conduct electricity) with broad common knowledge (e.g., a suit of armor is made of metal) obtained from other sources. While existing QA datasets over documents or knowledge bases, being generally self-contained, focus on linguistic understanding, OpenBookQA probes a deeper understanding of both the topic{---}in the context of common knowledge{---}and the language it is expressed in. Human performance on OpenBookQA is close to 92{\\%}, but many state-of-the-art pre-trained QA methods perform surprisingly poorly, worse than several simple neural baselines we develop. Our oracle experiments designed to circumvent the knowledge retrieval bottleneck demonstrate the value of both the open book and additional facts. We leave it as a challenge to solve the retrieval problem in this multi-hop setting and to close the large gap to human performance."\n}',
        anthology='mihaylov-etal-2018-suit',
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='MMLU',
        dataset_key=None,
        citation_key='hendrycks2021measuring',
        citation='@misc{hendrycks2021measuring,\n      title={Measuring Massive Multitask Language Understanding}, \n      author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},\n      year={2021},\n      eprint={2009.03300},\n      archivePrefix={arXiv},\n      primaryClass={cs.CY},\n      url={https://arxiv.org/abs/2009.03300}, \n}',
        anthology=None,
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='BBQ',
        dataset_key=None,
        citation_key='parrish-etal-2022-bbq',
        citation='@inproceedings{parrish-etal-2022-bbq,\n    title = "{BBQ}: A hand-built bias benchmark for question answering",\n    author = "Parrish, Alicia  and\n      Chen, Angelica  and\n      Nangia, Nikita  and\n      Padmakumar, Vishakh  and\n      Phang, Jason  and\n      Thompson, Jana  and\n      Htut, Phu Mon  and\n      Bowman, Samuel",\n    editor = "Muresan, Smaranda  and\n      Nakov, Preslav  and\n      Villavicencio, Aline",\n    booktitle = "Findings of the Association for Computational Linguistics: ACL 2022",\n    month = may,\n    year = "2022",\n    address = "Dublin, Ireland",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2022.findings-acl.165/",\n    doi = "10.18653/v1/2022.findings-acl.165",\n    pages = "2086--2105",\n    abstract = "It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question-sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. Our task evaluate model responses at two levels: (i) given an under-informative context, we test how strongly responses reflect social biases, and (ii) given an adequately informative context, we test whether the model{\'}s biases override a correct answer choice. We find that models often rely on stereotypes when the context is under-informative, meaning the model{\'}s outputs consistently reproduce harmful biases in this setting. Though models are more accurate when the context provides an informative answer, they still rely on stereotypes and average up to 3.4 percentage points higher accuracy when the correct answer aligns with a social bias than when it conflicts, with this difference widening to over 5 points on examples targeting gender for most models tested."\n}',
        anthology='parrish-etal-2022-bbq',
        languages=['EN'],
        license='cc-by-4.0'
    ),
    DatasetEntry(
        dataset='PIQA',
        dataset_key=None,
        citation_key='bist2020piqa',
        citation='@inproceedings{bist2020piqa,\n    author = {Yonatan Bisk and Rowan Zellers and\n            Ronan Le Bras and Jianfeng Gao\n            and Yejin Choi},\n    title = {PIQA: Reasoning about Physical Commonsense in\n           Natural Language},\n    booktitle = {Thirty-Fourth AAAI Conference on\n               Artificial Intelligence},\n    year = {2020},\n}',
        anthology=None,
        languages=['EN'],
        license='Apache 2.0'
    ),
    DatasetEntry(
        dataset='CommonsenseQA',
        dataset_key=None,
        citation_key='talmor-etal-2019-commonsenseqa',
        citation='@inproceedings{talmor-etal-2019-commonsenseqa,\n    title = "{C}ommonsense{QA}: A Question Answering Challenge Targeting Commonsense Knowledge",\n    author = "Talmor, Alon  and\n      Herzig, Jonathan  and\n      Lourie, Nicholas  and\n      Berant, Jonathan",\n    editor = "Burstein, Jill  and\n      Doran, Christy  and\n      Solorio, Thamar",\n    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",\n    month = jun,\n    year = "2019",\n    address = "Minneapolis, Minnesota",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/N19-1421/",\n    doi = "10.18653/v1/N19-1421",\n    pages = "4149--4158",\n    abstract = "When answering a question, people often draw upon their rich world knowledge in addition to the particular context. Recent work has focused primarily on answering questions given some relevant document or context, and required very little general background. To investigate question answering with prior knowledge, we present CommonsenseQA: a challenging new dataset for commonsense question answering. To capture common sense beyond associations, we extract from ConceptNet (Speer et al., 2017) multiple target concepts that have the same semantic relation to a single source concept. Crowd-workers are asked to author multiple-choice questions that mention the source concept and discriminate in turn between each of the target concepts. This encourages workers to create questions with complex semantics that often require prior knowledge. We create 12,247 questions through this procedure and demonstrate the difficulty of our task with a large number of strong baselines. Our best baseline is based on BERT-large (Devlin et al., 2018) and obtains 56{\\%} accuracy, well below human performance, which is 89{\\%}."\n}',
        anthology='talmor-etal-2019-commonsenseqa',
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='BBH',
        dataset_key=None,
        citation_key='suzgun-etal-2023-challenging',
        citation='@inproceedings{suzgun-etal-2023-challenging,\n    title = "Challenging {BIG}-Bench Tasks and Whether Chain-of-Thought Can Solve Them",\n    author = {Suzgun, Mirac  and\n      Scales, Nathan  and\n      Sch{\\"a}rli, Nathanael  and\n      Gehrmann, Sebastian  and\n      Tay, Yi  and\n      Chung, Hyung Won  and\n      Chowdhery, Aakanksha  and\n      Le, Quoc  and\n      Chi, Ed  and\n      Zhou, Denny  and\n      Wei, Jason},\n    editor = "Rogers, Anna  and\n      Boyd-Graber, Jordan  and\n      Okazaki, Naoaki",\n    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",\n    month = jul,\n    year = "2023",\n    address = "Toronto, Canada",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2023.findings-acl.824/",\n    doi = "10.18653/v1/2023.findings-acl.824",\n    pages = "13003--13051",\n    abstract = "BIG-Bench (Srivastava et al., 2022) is a diverse evaluation suite that focuses on tasks believed to be beyond the capabilities of current language models. Language models have already made good progress on this benchmark, with the best model in the BIG-Bench paper outperforming average reported human-rater results on 65{\\%} of the BIG-Bench tasks via few-shot prompting. But on what tasks do language models fall short of average human-rater performance, and are those tasks actually unsolvable by current language models? In this work, we focus on a suite of 23 challenging BIG-Bench tasks which we call BIG-Bench Hard (BBH). These are the tasks for which prior language model evaluations did not outperform the average human-rater. We find that applying chain-of-thought (CoT) prompting to BBH tasks enables PaLM to surpass the average human-rater performance on 10 of the 23 tasks, and Codex (code-davinci-002) to surpass the average human-rater performance on 17 of the 23 tasks. Since many tasks in BBH require multi-step reasoning, few-shot prompting without CoT, as done in the BIG-Bench evaluations (Srivastava et al., 2022), substantially underestimates the best performance and capabilities of language models, which is better captured via CoT prompting. As further analysis, we explore the interaction between CoT and model scale on BBH, finding that CoT enables emergent task performance on several BBH tasks with otherwise flat scaling curves."\n}',
        anthology='suzgun-etal-2023-challenging',
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='MATH',
        dataset_key=None,
        citation_key='hendrycksmath2021',
        citation='@article{hendrycksmath2021,\n    title={Measuring Mathematical Problem Solving With the MATH Dataset},\n    author={Dan Hendrycks\n    and Collin Burns\n    and Saurav Kadavath\n    and Akul Arora\n    and Steven Basart\n    and Eric Tang\n    and Dawn Song\n    and Jacob Steinhardt},\n    journal={arXiv preprint arXiv:2103.03874},\n    year={2021}\n}',
        anthology=None,
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='HumanEval',
        dataset_key=None,
        citation_key='chen2021evaluating',
        citation='@misc{chen2021evaluating,\n      title={Evaluating Large Language Models Trained on Code},\n      author={Mark Chen and Jerry Tworek and Heewoo Jun and Qiming Yuan and Henrique Ponde de Oliveira Pinto and Jared Kaplan and Harri Edwards and Yuri Burda and Nicholas Joseph and Greg Brockman and Alex Ray and Raul Puri and Gretchen Krueger and Michael Petrov and Heidy Khlaaf and Girish Sastry and Pamela Mishkin and Brooke Chan and Scott Gray and Nick Ryder and Mikhail Pavlov and Alethea Power and Lukasz Kaiser and Mohammad Bavarian and Clemens Winter and Philippe Tillet and Felipe Petroski Such and Dave Cummings and Matthias Plappert and Fotios Chantzis and Elizabeth Barnes and Ariel Herbert-Voss and William Hebgen Guss and Alex Nichol and Alex Paino and Nikolas Tezak and Jie Tang and Igor Babuschkin and Suchir Balaji and Shantanu Jain and William Saunders and Christopher Hesse and Andrew N. Carr and Jan Leike and Josh Achiam and Vedant Misra and Evan Morikawa and Alec Radford and Matthew Knight and Miles Brundage and Mira Murati and Katie Mayer and Peter Welinder and Bob McGrew and Dario Amodei and Sam McCandlish and Ilya Sutskever and Wojciech Zaremba},\n      year={2021},\n      eprint={2107.03374},\n      archivePrefix={arXiv},\n      primaryClass={cs.LG}\n}',
        anthology=None,
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='MBPP',
        dataset_key=None,
        citation_key='austin2021program',
        citation='@article{austin2021program,\n  title={Program Synthesis with Large Language Models},\n  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and Bosma, Maarten and Michalewski, Henryk and Dohan, David and Jiang, Ellen and Cai, Carrie and Terry, Michael and Le, Quoc and others},\n  journal={arXiv preprint arXiv:2108.07732},\n  year={2021}',
        anthology=None,
        languages=['EN'],
        license='cc-by-4.0'
    ),
    DatasetEntry(
        dataset='GSM8k',
        dataset_key=None,
        citation_key='cobbe2021training',
        citation='@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021}\n}',
        anthology=None,
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='GPQA',
        dataset_key=None,
        citation_key='rein2024gpqa',
        citation='@inproceedings{rein2024gpqa,\n      title={{GPQA}: A Graduate-Level Google-Proof Q\\&A Benchmark},\n      author={David Rein and Betty Li Hou and Asa Cooper Stickland and Jackson Petty and Richard Yuanzhe Pang and Julien Dirani and Julian Michael and Samuel R. Bowman},\n      booktitle={First Conference on Language Modeling},\n      year={2024},\n      url={https://openreview.net/forum?id=Ti67584b98}\n}',
        anthology=None,
        languages=['EN'],
        license='cc-by-4.0'
    ),
    DatasetEntry(
        dataset='MultiNativQA',
        dataset_key=None,
        citation_key='hasan2025nativqa',
        citation='@misc{hasan2025nativqa,\n      title={NativQA: Multilingual Culturally-Aligned Natural Query for LLMs}, \n      author={Md. Arid Hasan and Maram Hasanain and Fatema Ahmad and Sahinur Rahman Laskar and Sunaya Upadhyay and Vrunda N Sukhadia and Mucahid Kutlu and Shammur Absar Chowdhury and Firoj Alam},\n      year={2025},\n      eprint={2407.09823},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2407.09823}, \n}',
        anthology=None,
        languages=['EN'],
        license='cc-by-nc-sa-4.0'
    ),
    DatasetEntry(
        dataset='CulturalBench',
        dataset_key=None,
        citation_key='chiu2024culturalbench',
        citation='@misc{chiu2024culturalbench,\n      title={CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming}, \n      author={Yu Ying Chiu and Liwei Jiang and Bill Yuchen Lin and Chan Young Park and Shuyue Stella Li and Sahithya Ravi and Mehar Bhatia and Maria Antoniak and Yulia Tsvetkov and Vered Shwartz and Yejin Choi},\n      year={2025},\n      eprint={2410.02677},\n      archivePrefix={arXiv},\n      primaryClass={cs.CL},\n      url={https://arxiv.org/abs/2410.02677}, \n}',
        anthology=None,
        languages=['EN'],
        license='cc-by-4.0\n'
    ),
    DatasetEntry(
        dataset='SeaEval',
        dataset_key=None,
        citation_key='wang-etal-2024-seaeval',
        citation='@inproceedings{wang-etal-2024-seaeval,\n    title = "{S}ea{E}val for Multilingual Foundation Models: From Cross-Lingual Alignment to Cultural Reasoning",\n    author = "Wang, Bin  and\n      Liu, Zhengyuan  and\n      Huang, Xin  and\n      Jiao, Fangkai  and\n      Ding, Yang  and\n      Aw, AiTi  and\n      Chen, Nancy",\n    editor = "Duh, Kevin  and\n      Gomez, Helena  and\n      Bethard, Steven",\n    booktitle = "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",\n    month = jun,\n    year = "2024",\n    address = "Mexico City, Mexico",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2024.naacl-long.22/",\n    doi = "10.18653/v1/2024.naacl-long.22",\n    pages = "370--390",\n    abstract = "We present SeaEval, a benchmark for multilingual foundation models. In addition to characterizing how these models understand and reason with natural language, we also investigate how well they comprehend cultural practices, nuances, and values. Alongside standard accuracy metrics, we investigate the brittleness of foundation models in the dimensions of semantics and multilinguality. Our analyses span both open-sourced and closed models, leading to empirical results across classic NLP tasks, reasoning, and cultural comprehension. Key findings indicate (1) Many models exhibit varied behavior when given paraphrased instructions. (2) Many models still suffer from exposure bias (e.g., positional bias, majority label bias). (3) For questions rooted in factual, scientific, and commonsense knowledge, consistent responses are expected across multilingual queries that are semantically equivalent. Yet, most models surprisingly demonstrate inconsistent performance on these queries. (4) Multilingually-trained models have not attained ``balanced multilingual\'\' capabilities. Our endeavors underscore the need for more generalizable semantic representations and enhanced multilingual contextualization. SeaEval can serve as a launchpad for more thorough investigations and evaluations for multilingual and multicultural scenarios."\n}',
        anthology='wang-etal-2024-seaeval',
        languages=['EN'],
        license='cc-by-nc-4.0'
    ),
    DatasetEntry(
        dataset='CANDLE CCSK',
        dataset_key=None,
        citation_key='nguyen2023extracting',
        citation='@inproceedings{nguyen2023extracting,\n   title={Extracting Cultural Commonsense Knowledge at Scale},\n   url={http://dx.doi.org/10.1145/3543507.3583535},\n   DOI={10.1145/3543507.3583535},\n   booktitle={Proceedings of the ACM Web Conference 2023},\n   publisher={ACM},\n   author={Nguyen, Tuan-Phong and Razniewski, Simon and Varde, Aparna and Weikum, Gerhard},\n   year={2023},\n   month=apr, pages={1907–1917},\n   collection={WWW ’23} }',
        anthology=None,
        languages=['EN'],
        license='CC BY 4.0'
    ),
    DatasetEntry(
        dataset='GeoMLAMA',
        dataset_key=None,
        citation_key='yin-etal-2022-geomlama',
        citation='@inproceedings{yin-etal-2022-geomlama,\n    title = "{G}eo{MLAMA}: Geo-Diverse Commonsense Probing on Multilingual Pre-Trained Language Models",\n    author = "Yin, Da  and\n      Bansal, Hritik  and\n      Monajatipoor, Masoud  and\n      Li, Liunian Harold  and\n      Chang, Kai-Wei",\n    editor = "Goldberg, Yoav  and\n      Kozareva, Zornitsa  and\n      Zhang, Yue",\n    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",\n    month = dec,\n    year = "2022",\n    address = "Abu Dhabi, United Arab Emirates",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2022.emnlp-main.132/",\n    doi = "10.18653/v1/2022.emnlp-main.132",\n    pages = "2039--2055",\n    abstract = "Recent work has shown that Pre-trained Language Models (PLMs) store the relational knowledge learned from data and utilize it for performing downstream tasks. However, commonsense knowledge across different regions may vary. For instance, the color of bridal dress is white in American weddings whereas it is red in Chinese weddings. In this paper, we introduce a benchmark dataset, Geo-diverse Commonsense Multilingual Language Models Analysis (GeoMLAMA), for probing the diversity of the relational knowledge in multilingual PLMs. GeoMLAMA contains 3125 prompts in English, Chinese, Hindi, Persian, and Swahili, with a wide coverage of concepts shared by people from American, Chinese, Indian, Iranian and Kenyan cultures. We benchmark 11 standard multilingual PLMs on GeoMLAMA. Interestingly, we find that 1) larger multilingual PLMs variants do not necessarily store geo-diverse concepts better than its smaller variant; 2) multilingual PLMs are not intrinsically biased towards knowledge from the Western countries (the United States); 3) the native language of a country may not be the best language to probe its knowledge and 4) a language may better probe knowledge about a non-native country than its native country."\n}',
        anthology='yin-etal-2022-geomlama',
        languages=['EN'],
        license='unknown'
    ),
    DatasetEntry(
        dataset='NormAd',
        dataset_key=None,
        citation_key='rao-etal-2025-normad',
        citation='@inproceedings{rao-etal-2025-normad,\n    title = "{N}orm{A}d: A Framework for Measuring the Cultural Adaptability of Large Language Models",\n    author = "Rao, Abhinav Sukumar  and\n      Yerukola, Akhila  and\n      Shah, Vishwa  and\n      Reinecke, Katharina  and\n      Sap, Maarten",\n    editor = "Chiruzzo, Luis  and\n      Ritter, Alan  and\n      Wang, Lu",\n    booktitle = "Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",\n    month = apr,\n    year = "2025",\n    address = "Albuquerque, New Mexico",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2025.naacl-long.120/",\n    doi = "10.18653/v1/2025.naacl-long.120",\n    pages = "2373--2403",\n    ISBN = "979-8-89176-189-6",\n    abstract = "To be effectively and safely deployed to global user populations, large language models (LLMs) may need to adapt outputs to user values and cultures, not just know about them. We introduce NormAd, an evaluation framework to assess LLMs\' cultural adaptability, specifically measuring their ability to judge social acceptability across varying levels of cultural norm specificity, from abstract values to explicit social norms. As an instantiation of our framework, we create NormAd-Eti, a benchmark of 2.6k situational descriptions representing social-etiquette related cultural norms from 75 countries. Through comprehensive experiments on NormAd-Eti, we find that LLMs struggle to accurately judge social acceptability across these varying degrees of cultural contexts and show stronger adaptability to English-centric cultures over those from the Global South. Even in the simplest setting where the relevant social norms are provided, the best LLMs\' performance ($\\textless$ 82{\\%}) lags behind humans ($\\textgreater$ 95{\\%}). In settings with abstract values and country information, model performance drops substantially ($\\textless$ 60{\\%}), while human accuracy remains high ($\\textgreater$90{\\%}). Furthermore, we find that models are better at recognizing socially acceptable versus unacceptable situations. Our findings showcase the current pitfalls in socio-cultural reasoning of LLMs which hinder their adaptability for global audiences."\n}',
        anthology='rao-etal-2025-normad',
        languages=['EN'],
        license='cc-by-4.0'
    ),
    DatasetEntry(
        dataset='CultureBank',
        dataset_key=None,
        citation_key='shi-etal-2024-culturebank',
        citation='@inproceedings{shi-etal-2024-culturebank,\n    title = "{C}ulture{B}ank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies",\n    author = "Shi, Weiyan  and\n      Li, Ryan  and\n      Zhang, Yutong  and\n      Ziems, Caleb  and\n      Yu, Sunny  and\n      Horesh, Raya  and\n      Paula, Rog{\\\'e}rio Abreu De  and\n      Yang, Diyi",\n    editor = "Al-Onaizan, Yaser  and\n      Bansal, Mohit  and\n      Chen, Yun-Nung",\n    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",\n    month = nov,\n    year = "2024",\n    address = "Miami, Florida, USA",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2024.findings-emnlp.288/",\n    doi = "10.18653/v1/2024.findings-emnlp.288",\n    pages = "4996--5025",\n    abstract = "To enhance language models\' cultural awareness, we design a generalizable pipeline to construct cultural knowledge bases from different online communities on a massive scale. With the pipeline, we construct CultureBank, a knowledge base built upon users\' self-narratives with 12K cultural descriptors sourced from TikTok and 11K from Reddit. Unlike previous cultural knowledge resources, CultureBank contains diverse views on cultural descriptors to allow flexible interpretation of cultural knowledge, and contextualized cultural scenarios to help grounded evaluation. With CultureBank, we evaluate different LLMs\' cultural awareness, and identify areas for improvement. We also fine-tune a language model on CultureBank: experiments show that it achieves better performances on two downstream cultural tasks in a zero-shot setting. Finally, we offer recommendations for future culturally aware language technologies. We release the CultureBank dataset, code and models at https://github.com/SALT-NLP/CultureBank. Our project page is at culturebank.github.io"\n}',
        anthology='shi-etal-2024-culturebank',
        languages=['EN'],
        license='MIT'
    ),
    DatasetEntry(
        dataset='KorNAT',
        dataset_key=None,
        citation_key='lee-etal-2024-kornat',
        citation='@inproceedings{lee-etal-2024-kornat,\n    title = "{K}or{NAT}: {LLM} Alignment Benchmark for {K}orean Social Values and Common Knowledge",\n    author = "Lee, Jiyoung  and\n      Kim, Minwoo  and\n      Kim, Seungho  and\n      Kim, Junghwan  and\n      Won, Seunghyun  and\n      Lee, Hwaran  and\n      Choi, Edward",\n    editor = "Ku, Lun-Wei  and\n      Martins, Andre  and\n      Srikumar, Vivek",\n    booktitle = "Findings of the Association for Computational Linguistics: ACL 2024",\n    month = aug,\n    year = "2024",\n    address = "Bangkok, Thailand",\n    publisher = "Association for Computational Linguistics",\n    url = "https://aclanthology.org/2024.findings-acl.666/",\n    doi = "10.18653/v1/2024.findings-acl.666",\n    pages = "11177--11213",\n    abstract = "To reliably deploy Large Language Models (LLMs) in a specific country, they must possess an understanding of the nation{\'}s culture and basic knowledge. To this end, we introduce National Alignment, which measures the alignment between an LLM and a targeted country from two aspects: social value alignment and common knowledge alignment. We constructed KorNAT, the first benchmark that measures national alignment between LLMs and South Korea. KorNat contains 4K and 6K multiple-choice questions for social value and common knowledge, respectively. To attain an appropriately aligned ground truth in the social value dataset, we conducted a large-scale public survey with 6,174 South Koreans. For common knowledge, we created the data based on the South Korea text books and GED exams. Our dataset creation process is meticulously designed based on statistical sampling theory, and we also introduce metrics to measure national alignment, including three variations of social value alignment. We tested seven LLMs and found that only few models passed our reference score, indicating there exists room for improvement. Our dataset has received government approval following an assessment by a government-affiliated organization dedicated to evaluating dataset quality."\n}',
        anthology='lee-etal-2024-kornat',
        languages=['EN'],
        license='cc-by-nc-2.0'
    ),
]
