import os

from QuoteEngine import CSVIngestor, PDFIngestor, DocxIngestor, TextIngestor, Ingestor, Quote


TEST_FILE_DIR = os.path.join('tests', 'SimpleLines')
TEST_CSV = os.path.join(TEST_FILE_DIR, 'SimpleLines.csv')
TEST_PDF = os.path.join(TEST_FILE_DIR, 'SimpleLines.pdf')
TEST_TXT = os.path.join(TEST_FILE_DIR, 'SimpleLines.txt')
TEST_DOCX = os.path.join(TEST_FILE_DIR, 'SimpleLines.docx')
TEST_QUOTES = [Quote('Line 1', 'Author 1'),
               Quote('Line 2', 'Author 2'),
               Quote('Line 3', 'Author 3'),
               Quote('Line 4', 'Author 4'),
               Quote('Line 5', 'Author 5')]


def test_csv_ingestor_can_ingest_csv():
    assert CSVIngestor.can_ingest('file.csv')


def test_csv_ingestor_can_ingest_non_csv():
    assert not CSVIngestor.can_ingest('file.pdf')


def test_csv_ingestor_parse():
    assert CSVIngestor.parse(TEST_CSV) == TEST_QUOTES


def test_pdf_ingestor_parse():
    assert PDFIngestor.parse(TEST_PDF) == TEST_QUOTES


def test_docx_ingestor_parse():
    assert DocxIngestor.parse(TEST_DOCX) == TEST_QUOTES


def test_text_ingestor_parse():
    assert TextIngestor.parse(TEST_TXT) == TEST_QUOTES


def test_ingestor_parse_text():
    assert Ingestor.parse(TEST_TXT) == TEST_QUOTES


def test_ingestor_parse_pdf():
    assert Ingestor.parse(TEST_PDF) == TEST_QUOTES


def test_ingestor_parse_csv():
    assert Ingestor.parse(TEST_CSV) == TEST_QUOTES


def test_ingestor_parse_docx():
    assert Ingestor.parse(TEST_DOCX) == TEST_QUOTES
