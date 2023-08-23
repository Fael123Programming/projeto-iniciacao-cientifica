import openai, pandas, decouple, os, time

# Generate class, uncomment the following variables.
SOURCE_PATH = 'C:\\Users\\Rafae\\OneDrive\\Documentos\\projeto_iniciacao_cientifica\\ifgoiano_site\\datasets\\clean'
TARGET_PATH = 'C:\\Users\\Rafae\\OneDrive\\Documentos\\projeto_iniciacao_cientifica\\ifgoiano_site\\datasets\\class'

# Generate inter_class, uncomment the following variables.
# SOURCE_PATH = 'C:\\Users\\Rafae\\OneDrive\\Documentos\\projeto_iniciacao_cientifica\\ifgoiano_site\\datasets\\inter'
# TARGET_PATH = 'C:\\Users\\Rafae\\OneDrive\\Documentos\\projeto_iniciacao_cientifica\\ifgoiano_site\\datasets\\inter_class'


if __name__ == '__main__':
    key = decouple.config('API_KEY')
    files = os.listdir(SOURCE_PATH)
    content = "De acordo com os temas: ações de extensão, comunicados oficiais, conquistas de membros do IF Goiano (premiações), campanhas (covid-19, etc), editais, processos seletivos, publicações (obras literárias, boletins, etc) e avaliações, escolha um para o seguinte texto (escreva apenas o tema): '{}' '{}'"
    
    for f in files:
        csv = pandas.read_csv(os.path.join(SOURCE_PATH, f))
        csv = csv.reset_index()
        csv['subject'] = '-'
        print('-' * 100)
        for i in range(csv.shape[0]):
            title, description = csv.iloc[i][['titulo', 'descricao']]
            response = openai.ChatCompletion.create(
                api_key=key,
                model='gpt-3.5-turbo',
                messages=[
                    {
                        'role': 'user',
                        'content': content.format(
                            title,
                            description
                        )
                    }
                ]
            )
            answer = response['choices'][0]['message']['content']
            csv.loc[i, 'subject'] = answer
            print(f'({i + 1})')
            print(f'Title: {title}')
            print(f'Description: {description}')
            print(f'Subject: {answer.upper()}')
            print('-' * 100)
            time.sleep(25)
        csv.to_csv(os.path.join(TARGET_PATH, f), index=False)
        break