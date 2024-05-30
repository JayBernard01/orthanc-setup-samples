from pyorthanc import Orthanc, find_patients

def main():
    orthanc = Orthanc(url='http://localhost:8053/', username='orthanc', password='orthanc')
    patients = find_patients(
        client=orthanc
    )
    patient = patients[0]
    print(patient.name)

if __name__ == "__main__":
    main()
