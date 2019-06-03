import TwitterExtractor
import TextAnalysis
import Result

def run():
    term = input('Digite o usuário @ do twitter: ')
    print('\nExtraindo tweets...')
    TwitterExtractor.search(term)
    print('\nTweets extraidos!')
    print('\nIniciando processo de análise...')
    TextAnalysis.analisarTexto()
    print('\nAnálise concluída! Shutting down...')

run()
