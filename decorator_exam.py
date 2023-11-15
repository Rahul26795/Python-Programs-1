#Here we have an example of decorater in pythob


def details(data):
    def skill():
        print("Here are the skills that are avaiable")
        skills = ['Drawing','Analaysis','Mathematical Modeling','Mining of the data']
        for sk in range(len(skills)):
            print(skills[sk])
        data()
    return skill

@details

def hobby():
    print(" \n\n\n  Here are my List of hobbies")
    print("\n Watching Documentary \n Journalling \n Watching tech videos \n")


print("Hi There!!  Below are some of the details that you find interesting ")
hobby()