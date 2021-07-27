import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Screenshot import Screenshot_Clipping
from subprocess import run, DEVNULL
import argparse


# # # ---------- BASIC_SETUP ---------- # # #
parser = argparse.ArgumentParser()
parser.add_argument('-W', '--webbrowser', help='Path to webbrowser executable. See: config file')
parser.add_argument('-I', '--iterations', help='Number of iterations')
parser.add_argument('-F', '--file', help='Absolute path to input file')
parser.add_argument('-B', '--base', help='Image and summary file name base')
args = parser.parse_args()
DRIVER_PATH = args.webbrowser
driver = webdriver.Chrome(DRIVER_PATH)
driver.maximize_window()


# # --- Input text from file ---
# element = driver.find_element_by_id("seq")
# element.send_keys("some text")


def jump_to_download(c_url):  # - Download
    url = c_url.split('/')
    url[5] = 'download'
    url.append('?format=fasta')
    url = '/'.join(url)
    return url


def iteration_process(iters, file):
    def input_first_iter(file_directory):
        # ---------- Input file and start 1 iteration ----------
        open_jackhmmer = driver.get("https://www.ebi.ac.uk/Tools/hmmer/search/jackhmmer")
        privacy_banner_close = driver.find_element_by_xpath('// *[ @ id = "data-protection-agree"]').click()
        change_tab = driver.find_element_by_xpath('//*[@id="iterativeSearchForm"]/div[1]/p/a[2]').click()
        submit_file = driver.find_element_by_id('file').send_keys(file_directory)
        begin_iter = driver.find_element_by_xpath('//*[@id="subbutton"]').submit()


    def submit_X_path(x_path):
        # ---------- Start next iteration ----------
        counter = 0
        while True:
            try:
                if counter == 50:
                    return 0
                begin_iter = driver.find_element_by_xpath(x_path).submit()
                return counter
            except:
                time.sleep(1)
                counter += 1
                continue

    if iters < 1:
        print('0 Iters?')
    else:
        for i in range(iters):
            if i == 0:
                input_first_iter(file)
            elif i == 1:
                second_iteration = submit_X_path('//*[@id="next_iteration"]/p/input')
            else:
                next_iteration = submit_X_path('//*[@id="next_iteration"]/input[3]')
    base_url = driver.current_url
    return base_url


def get_resutls_pages(iters, base_name, base_url):
    def go_to_domain_summary(iter_number, url):
        url = url.split('/')
        url[-2] = f'{url[-2].split(".")[0]}.{iter_number + 1}'
        url[-1] = 'domain'
        url = '/'.join(url)
        try:                            #
            driver.get(url)             #
        except:                         #
            print('Timeout Exception')  #
            driver.get(url)             #
        error = driver.find_element_by_xpath('//*[@id="error"]').text
        if 'Please wait for the search to complete.' in error:
            time.sleep(2)
            go_to_domain_summary(iter_number, url)
        return url

    def take_screenshot(name):
        Hide_elements = ['class= masthead row', 'class= sticky-container', 'id=global-footer', 'id=local-footer', 'class=actions', 'class=small pop-button right', 'class=meta', 'id=subnav', 'class=float-right reuse button small', 'class=notify nojshide release-info important', 'class=columns small-6 medium-6', 'class=left']
        ob = Screenshot_Clipping.Screenshot()
        img_url = ob.full_Screenshot(driver, save_path=r'', elements=Hide_elements, image_name=name)
        print(img_url)

    def get_links(url):
        domains = []
        description = driver.find_elements_by_xpath('//*[@id="content"]/div[5]/ul[2]/li/p')
        for i in description:
            if 'with' in i.text:
                if 'no' in i.text:
                    domains.append('No architecture')
                else:
                    domains.append(i.text.split(':')[1].split(',')[:-1])

        number_of_seqs = []
        part2 = driver.find_elements_by_xpath('//*[@id="content"]/div[5]/ul/li/a')
        for i in part2:
            number_of_seqs.append(i.text.split('\n')[0])

        details_links = []
        part3 = driver.find_elements_by_xpath('//*[@id="content"]/div[5]/ul/li/a')
        for i in part3:
            details_links.append(i.get_attribute('href'))
        return domains, number_of_seqs, details_links

    data_to_summary = []
    for i in range(iters):
        current_url = go_to_domain_summary(i, base_url)
        take_screenshot(f'{base_name}{i}.png')
        dom, num, det = get_links(current_url)
        data_to_summary.append([dom, num, det, current_url])

    return data_to_summary


def prepare_summary_document(doc_base_name, image_base, iterations, data):
    def initialize_doc(doc):
        doc.write(r'''\documentclass[12pt]{article}

\usepackage[margin=0.5in]{geometry}

\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=blue,
}
 
\urlstyle{same}

\usepackage{polski}
\usepackage[polish]{babel}
\usepackage[utf8]{inputenc}

\usepackage{titling}

\usepackage{graphicx}
\graphicspath{ {./images/} }

\usepackage{verbatim}''')
        doc.write('\n')

    def main_part(doc, image, iters, data):
        doc.write(r'\begin{document}')
        doc.write('\n')
        '''
	\item \href{https://www.uniprot.org/help/}{Strona pomocy w Uniprot}
        '''
        for i in range(iters):
            try:
                doc.write(r'\href{' + data[i][3] + '}{')
                doc.write(f'Iteration {i+1}')
                doc.write('}\n')
                doc.write(r'\begin{itemize}')
                doc.write('\n')
                for i1 in range(len(data[i][1])):
                    doc.write(r'\item ')
                    for i2 in range(len(data[i][0][i1])):
                        text = data[i][0][i1][i2]
                        if '_' in text:
                            text2 = text.replace('_', r'\_')
                            doc.write(text2)
                        else:
                            doc.write(text)
                    doc.write(' - ')
                    doc.write(data[i][1][i1])
                    doc.write(' Sequences')
                    doc.write(r' \href{')
                    doc.write(data[i][2][i1])
                    doc.write(r'}{')
                    doc.write('LINK')
                    doc.write('}\n')
                doc.write(r'\end{itemize}')
                doc.write('\n')
                doc.write(r'\begin{figure}[h]')
                doc.write('\n')
                doc.write(r'\includegraphics[width=\textwidth]{' + f'{image}{i}' + '}')
                doc.write('\n')
                doc.write(r'\end{figure}')
                doc.write('\n')
                doc.write(r'\newpage')
                doc.write('\n')
            except IndexError:
                doc.write('Run finished (Nothing more found or search took too long to finish)!')
        doc.write(r'\end{document}')

    def generate_pdf(doc_base_name):
        run(f'pdflatex -synctex=1 -interaction=nonstopmode {doc_base_name}.tex', shell=True, stdout=DEVNULL)

    def cleanup():
        list_to_delete = ['.aux', '.log', '.out', '.synctex.gz', '.tex']
        for i in list_to_delete:
            run(f'rm ./{doc_base_name}{i}', shell=True)

    def move_to_destination(doc_base_name, dir):
        run(f'mv {doc_base_name}.pdf {dir}', shell=True)


    summary = open(f'{doc_base_name}.tex', 'w')
    initialize_doc(summary)
    main_part(summary, image_base, iterations, data)
    summary.close()
    generate_pdf(doc_base_name)
    cleanup()
    move_to_destination(doc_base_name, r'./summary')


def main():
    number_of_iters = int(args.iterations)
    file = args.file
    file_base = args.base
    base_url = iteration_process(number_of_iters, file)
    summary_data = get_resutls_pages(number_of_iters, f'images/{file_base}_iter_', base_url)
    prepare_summary_document(file_base, f'{file_base}_iter_', number_of_iters, summary_data)
    driver.quit()


main()

# Max Seq: 500
# Max lines: 5.000