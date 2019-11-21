import csv
import sys
import os

def write_csv(output_csv, output_csv_rows, header):
    """ Writes a list of csv data to a csv file

    Parameters
    ----------
        output_csv (str): The output file
        output_csv_rows (list): The output file's input
    """

    try:
        os.mkdir("./csv_outputs")     # make a folder to store the output files
    except OSError as e:
        pass                              # do nothing if folder already exists

    path = './csv_outputs/' + output_csv
    with open(path, 'w+') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)                     # write the header to output
        for row in output_csv_rows:
            f_csv.writerow(row)             # write each row to the output file

def main():
    input_csv = sys.argv[1]                        # get the input csv filename

    # initialize the output csv files
    output_200 = input_csv[:-4] + '_200.csv'
    output_200_rows = []
    output_redirection = input_csv[:-4] + '_redirection.csv'
    output_redirection_rows = []
    output_302 = input_csv[:-4] + '_302.csv'
    output_302_rows = []
    output_400 = input_csv[:-4] + '_400.csv'
    output_400_rows = []
    output_403 = input_csv[:-4] + '_403.csv'
    output_403_rows = []
    output_404 = input_csv[:-4] + '_404.csv'
    output_404_rows = []
    output_503 = input_csv[:-4] + '_503.csv'
    output_503_rows = []
    output_504 = input_csv[:-4] + '_504.csv'
    output_504_rows = []
    output_urlerr = input_csv[:-4] + '_urlerr.csv'
    output_urlerr_rows = []
    output_err_104 = input_csv[:-4] + '_err_104.csv'
    output_err_104_rows = []
    output_no_match = input_csv[:-4] + '_no_match.csv'
    output_no_match_rows = []
    output_closed = input_csv[:-4] + '_closed.csv'
    output_closed_rows = []

    # initialize all possible messages
    msg_200 = 'Return code 200'
    msg_redirection = 'Redirected to'
    msg_302 = 'HTTPError: 302'
    msg_400 = 'HTTPError: 400'
    msg_403 = 'HTTPError: 403'
    msg_404 = 'HTTPError: 404'
    msg_503 = 'HTTPError: 503'
    msg_504 = 'HTTPError: 504'
    msg_urlerr = 'URLError'
    msg_err_104 = '[Errno 104] Connection reset by peer'
    msg_no_match = 'doesn\'t match'
    msg_closed = 'Remote end closed connection'

    # initialize the counters for each scenario
    count_200 = 0
    count_redirection = 0
    count_302 = 0
    count_400 = 0
    count_403 = 0
    count_404 = 0
    count_503 = 0
    count_504 = 0
    count_urlerr = 0
    count_err_104 = 0
    count_no_match = 0
    count_closed = 0
    count_total = 0

    with open(input_csv) as f:

        f_csv = csv.reader(f)                             # init the csv reader

        header = next(f_csv)                            # get the header of csv

        for row in f_csv:

            count_total += 1         # increment count_total when reading a row

            site_status = row[3]                          # either LIVE or FAIL
            site_msg = row[4]

            if site_status == 'LIVE':                     # if the site is LIVE
                if site_msg == msg_200:                                # if 200
                    count_200 += 1
                    output_200_rows.append(row)
                elif msg_redirection in site_msg:               # if redirecion
                    count_redirection += 1
                    output_redirection_rows.append(row)
                else:
                    print(row)            # just in case of uncovered scenarios
            else:                                         # if the site is FAIL
                if site_msg == msg_302:                                # if 302
                    count_302 += 1
                    output_302_rows.append(row)
                elif site_msg == msg_400:                              # if 400
                    count_400 += 1
                    output_400_rows.append(row)
                elif site_msg == msg_403:                              # if 403
                    count_403 += 1
                    output_403_rows.append(row)
                elif site_msg == msg_404:                              # if 404
                    count_404 += 1
                    output_404_rows.append(row)
                elif site_msg == msg_503:                              # if 503
                    count_503 += 1
                    output_503_rows.append(row)
                elif site_msg == msg_504:                              # if 504
                    count_504 += 1
                    output_504_rows.append(row)
                elif msg_urlerr in site_msg:                     # if url error
                    count_urlerr += 1
                    output_urlerr_rows.append(row)
                elif site_msg == msg_err_104:                    # if error 104
                    count_err_104 += 1
                    output_err_104_rows.append(row)
                elif msg_no_match in site_msg:                    # if no match
                    count_no_match += 1
                    output_no_match_rows.append(row)
                elif msg_closed in site_msg:             # if closed connection
                    count_closed += 1
                    output_closed_rows.append(row)
                else:
                    print(row)            # just in case of uncovered scenarios

    # write the output rows to different output files
    write_csv(output_200, output_200_rows, header)
    write_csv(output_redirection, output_redirection_rows, header)
    write_csv(output_302, output_302_rows, header)
    write_csv(output_400, output_400_rows, header)
    write_csv(output_403, output_403_rows, header)
    write_csv(output_404, output_404_rows, header)
    write_csv(output_503, output_503_rows, header)
    write_csv(output_504, output_504_rows, header)
    write_csv(output_urlerr, output_urlerr_rows, header)
    write_csv(output_err_104, output_err_104_rows, header)
    write_csv(output_no_match, output_no_match_rows, header)
    write_csv(output_closed, output_closed_rows, header)

    # calculating the rates of each scenario
    rate_200 = count_200 / count_total
    rate_redirection = count_redirection / count_total
    rate_302 = count_302 / count_total
    rate_400 = count_400 / count_total
    rate_403 = count_403 / count_total
    rate_404 = count_404 / count_total
    rate_503 = count_503 / count_total
    rate_504 = count_504 / count_total
    rate_urlerr = count_urlerr / count_total
    rate_err_104 = count_err_104 / count_total
    rate_no_match = count_no_match / count_total
    rate_closed = count_closed / count_total

    # print a summary of results
    print('\nThe output files are stored in \"csv_outputs\" folder.\n')
    print('Total number of urls: {}\n'.format(count_total))
    print('Number of urls returning 200: {}'.format(count_200))
    print('Rate of urls returning 200: {0:.2f}%\n'.format(rate_200))
    print('Number of redirections: {}'.format(count_redirection))
    print('Rate of redirections: {0:.2f}%\n'.format(rate_redirection))
    print('Number of urls returning 302: {}'.format(count_302))
    print('Rate of urls returning 302: {0:.2f}%\n'.format(rate_302))
    print('Number of urls returning 400: {}'.format(count_400))
    print('Rate of urls returning 400: {0:.2f}%\n'.format(rate_400))
    print('Number of urls returning 403: {}'.format(count_403))
    print('Rate of urls returning 403: {0:.2f}%\n'.format(rate_403))
    print('Number of urls returning 404: {}'.format(count_404))
    print('Rate of urls returning 404: {0:.2f}%\n'.format(rate_404))
    print('Number of urls returning 503: {}'.format(count_503))
    print('Rate of urls returning 503: {0:.2f}%\n'.format(rate_503))
    print('Number of urls returning 504: {}'.format(count_504))
    print('Rate of urls returning 504: {0:.2f}%\n'.format(rate_504))
    print('Number of urls with errors: {}'.format(count_urlerr))
    print('Rate of urls with errors: {0:.2f}%\n'.format(rate_urlerr))
    print('Number of urls returning error 104: {}'.format(count_err_104))
    print('Rate of urls returning error 104: {0:.2f}%\n'.format(rate_err_104))
    print('Number of urls not matching: {}'.format(count_no_match))
    print('Rate of urls not matching: {0:.2f}%\n'.format(rate_no_match))
    print('Number of urls having closed connection: {}'.format(count_closed))
    print('Rate of urls having closed connection: {0:.2f}%\n'.format(rate_closed))

main()
