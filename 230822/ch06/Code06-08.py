<<<<<<< HEAD
import csv
# csv 파일 두개를 합치는 예제
with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA:
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum_230822.csv", "w", newline='') as outFp:
=======
# csv 2개를 하나의 csv 합치는 예제.
import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA:
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum_230822.csv", "w", newline='') as outFp:
            # csv 모듈의 함수를 이용해서, 읽기 및 쓰기 작업을함.
>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)

<<<<<<< HEAD
            # 2개의 csv 파일의 구조가 동일해서 하나로 덮어쓰기
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # cvs 파일을 쓰는 작업
            csvWriter.writerow(header_list)

            # 2 행부터 실제 데이터 값 쓰기
=======
            # 2개의 csv 파일의 구조가 동일 해서,
            # 헤더가  동일해서, 덮어쓰기.
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # csv 파일을 쓰는 작업 컬럼.
            csvWriter.writerow(header_list)

            # 2행 부터 실제 데이터 값.
            # csv 첫번째 파일을 쓰고
            # csv 두번째 파일을 쓰기.
>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')
