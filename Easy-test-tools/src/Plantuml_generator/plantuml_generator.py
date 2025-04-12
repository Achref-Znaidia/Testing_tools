# generate plantuml diagram from steps
from py2puml.py2puml import py2puml

if __name__ == '__main__':
    # outputs the PlantUML content in the terminal
    print(''.join(py2puml('py2puml/domain', 'py2puml.domain')))

    # writes the PlantUML content in a file
    with open('py2puml/py2puml.domain.puml', 'w', encoding='utf8') as puml_file:
        puml_file.writelines(py2puml('py2puml/domain', 'py2puml.domain'))


import py2puml
import plantuml
# Generate images from py2puml



#Generate images from plantuml defined files using plantuml server
def generate(filename):
    diagram = plantuml.generate(filename)
    return diagram

plantuml = plantuml.PlantUML()
#Generate images from plantuml defined files using plantuml server
def generate_sequence_diagram(filename):
    diagram = plantuml.generate(filename)
    return diagram

if __name__ == '__main__':
    diagram = generate_sequence_diagram("C:\\Users\\asus\\Desktop\\testing_tools\\Testing_tools\\Easy-test-tools\\src\\Plantuml_generator\\sample.txt")
    diagram.save("C:\\Users\\asus\\Desktop\\testing_tools\\Testing_tools\\Easy-test-tools\\src\\Plantuml_generator\\sample.png")