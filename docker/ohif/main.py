from pyorthanc import Orthanc, find_patients

#TODO add anonymisation via python
#TODO add study via python
#TODO add queue for anonymise -> using django and celery -> queue the anonymise process async and store json config for log
#TODO apply conversions if needed to dicom
#TODO review existing solutions for each part with Azure -> ce qui existe pour Azure est clé en main, mais n'utilise pas ORTHANC, vaut mieux l'apprendre par nous-même

def main():
    orthanc = Orthanc(url='http://localhost:8053/', username='orthanc', password='orthanc')
    patients = find_patients(
        client=orthanc
    )
    patient = patients[0]
    print(patient.name)

if __name__ == "__main__":
    main()
