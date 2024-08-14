import pandas as pd
from collections import OrderedDict


def clean(x):
    """

    :param x: input string
    :return: a cleaned string, lower case and stripped off leading and trailing whitespace
    """
    if isinstance(x, str):
        x = x.lower().strip()
    return x


def dataset_socket(input_df):
    """

    :param input_df: input dataframe
    :return: a cleaned up dataframe
    """
    output_df = pd.DataFrame()

    # output_df['file'] = input_df['ID'].apply(lambda x: f'file{x}')
    output_df['DOI'] = input_df['DOI'].apply(clean)
    output_df['citation_marker'] = input_df['Citation marker'].apply(clean)
    output_df['paragraph'] = input_df['Citation context']
    output_df['Q1 - Review article? (Scopus)'] = input_df['Q1 - Review article? (Scopus)'].apply(clean)
    output_df['Q1 - Review article? (WoS)'] = input_df['Q1 - Review article? (WoS)'].apply(clean)
    output_df['Q2 - Addendum or Neupane? (Scopus)'] = input_df['Q2 - Addendum or Neupane? (Scopus)'].apply(clean)
    output_df['Q2 - Addendum or Neupane? (WoS)'] = input_df['Q2 - Addendum or Neupane? (WoS)'].apply(clean)
    output_df['section'] = input_df['Introduction section?'].apply(clean)
    # output_df['is_multicitation'] = input_df['Number of citation contexts'].apply(
    #     lambda x: 'True' if x > 1 else 'False')
    return output_df


def data_ingestion_s2(data):
    """
    :param data: input data
    :return: a publication dictionary for stage 2 assessment
    """
    pub_dict = OrderedDict()

    for index, row in data.iterrows():
        file_name = row['DOI']

        if file_name not in pub_dict:
            pub_dict[file_name] = {'citation_context': []}

        pub_dict[file_name]['citation_context'].append({'citation_marker': row['citation_marker'],
                                                        'section': row['section'],
                                                        'paragraph': row['paragraph']})
    return pub_dict


def is_only_in_introduction(dict_item):
    """

    :param dict_item: a dictionary item with keys 'DOI' and 'citation_context'
    :return: whether citation context only appears in the introduction section
    """
    section_l = []
    for x in dict_item['citation_context']:
        section_l.append(x['section'])

    if set(section_l) == {'y'}:
        return True
    else:
        return False


# def data_ingestion_s3(data):
#     """
#     :param data: input data
#     :return: a publication dictionary for stage 3 assessment
#     """
#     pub_dict = OrderedDict()
#
#     for _, row in data.iterrows():
#         file_name = row['DOI']
#         print(file_name)
#
#         if file_name not in pub_dict:
#             pub_dict[file_name] = {'citation_context': []}
#
#         pub_dict[file_name]['citation_context'].append([{'sent': row['Citation context (sent)']}])
#
#         print(row['Citation context (sent)'])
#
#     return pub_dict

def keyword_dict_construction(keyword_dict_file_path):
    """

    :param keyword_dict_file_path:
    :return: a keyword dictionary
    """
    keyword_df = pd.read_csv(keyword_dict_file_path)
    keyword_df['keyword'] = keyword_df['keyword'].apply(clean)

    keyword_dict = {'reducing': [],
                    'elevating': []}

    for index, row in keyword_df.iterrows():
        risk = row['risk']
        keyword_dict[risk].append(row['keyword'])

    return keyword_dict


def keyword_detection(dict_item, keyword_dict):
    """

    :param dict_item: a dictionary item
    :param keyword_dict:
    :return: a dictionary with two keys: elevating and reducing, values as the keywords detected
    """

    detection_dict = {'reducing': [], 'elevating': [], 'all_reducing': True}

    for context in dict_item['citation_context']:

        sent = context['sent']

        if type(sent) == str:
            reducing_dict_len_track = len(detection_dict['reducing'])

            for keyword in keyword_dict['reducing']:
                if keyword in clean(sent):
                    detection_dict['reducing'].append(keyword)

            if len(detection_dict['reducing']) == reducing_dict_len_track:
                detection_dict['all_reducing'] = False

            for keyword in keyword_dict['elevating']:
                if keyword in clean(sent):
                    detection_dict['elevating'].append(keyword)

    return detection_dict




