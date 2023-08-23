import pandas


if __name__ == '__main__':
    PATH = 'C:\\Users\\Rafae\\OneDrive\\Documentos\\projeto_iniciacao_cientifica\\ifgoiano_site\\chatgpt\\archive.csv'
    csv = pandas.read_csv(PATH)
    csv['subject'] = '-'
    csv.loc[1, 'name'] = 'Gilmar'
    csv.loc[1, 'subject'] = 'Programador fodao'
    csv.to_csv(PATH, index=False)