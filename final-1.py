import asyncio

class WallysTrainingGym:
    """
    Name of the submission: Trainers/Enrollees
    Author of the submission: Bailey Dunlap

    Summary/goal of the submission: The code allows a gym to track the number of new enrollees for each trainer and displays a summary of enrollment based on different categories of new members.

    trainers: A list that stores the last name of each trainer. Data type: list of strings.
    enrollees: A list that stores the number of new enrollees for each trainer. Data type: list of integers.
    num_trainers: An integer variable that stores the number of trainers enrolled. Data type: integer.
    category_counts: A list that stores the count of new enrollees based on categories: 0-5, 6-10, 11-15. Data type: list of integers.
    enrollee_count: An integer variable that stores the number of new enrollees for each trainer. Data type: integer.
    last_name: A string variable that stores the last name of the trainer. Data type: string.
    num_enrollees: An integer variable that stores the number of new enrollees for the trainer. Data type: integer.
    """
    def __init__(self):
        self.trainers = [] # initialize an empty list to keep track of trainers
        self.enrollees = [] # initialize an empty list to keep track of number of new enrollees

    async def enroll(self):
        """
        This method allows a trainer to enroll new members by inputting the last name of the trainer and 
        the number of new enrollees. The last name and number of new enrollees are then appended to 
        self.trainers and self.enrollees respectively.
        """
        print("Enter the last name of the trainer and the number of new enrollees:")
        last_name = input("Trainer's last name: ")
        num_enrollees = int(input("Number of new enrollees: "))

        self.trainers.append(last_name)
        self.enrollees.append(num_enrollees)

    async def display_enrollment_summary(self):
        """
        This method displays the enrollment summary for all trainers who enrolled new members. 
        It prints the total number of trainers who enrolled new members and the number of new members 
        in each of the three categories (0-5, 6-10, and 11-15).
        """
        num_trainers = len(self.trainers) # get the total number of trainers who enrolled new members

        if num_trainers == 0:
            print("No trainers enrolled any new members.") # if there are no trainers, print a message and return
            return

        category_counts = [0, 0, 0] # initialize a list to keep track of the number of new members in each category (0-5, 6-10, 11-15)

        for enrollee_count in self.enrollees:
            # loop through all the enrollee counts and add them to the appropriate category
            if enrollee_count <= 5:
                category_counts[0] += 1
            elif enrollee_count <= 10:
                category_counts[1] += 1
            else:
                category_counts[2] += 1

        # print the enrollment summary with f-strings
        print(f"""Enrollment summary for {num_trainers} trainers:\n0-5 new members: {category_counts[0]}\n6-10 new members: {category_counts[1]}\n11-15 new members: {category_counts[2]}""")

    async def run(self):
        """
        This method runs the enrollment system by calling the enroll method 15 times and then 
        displaying the enrollment summary.
        """
        print("Wally's Training Gym Enrolment System\n------------------------------------")

        for _ in range(15):
            await self.enroll() # call the enroll method 15 times

        await self.display_enrollment_summary() # display the enrollment summary

if __name__ == '__main__':
    gym = WallysTrainingGym()
    asyncio.run(gym.run()) # create a WallysTrainingGym object and run the enrollment system using asyncio module

