class UserInputValidator:
    def __init__(self):
        """creating the validator with an empty list"""
        self.validated_data = []

    def validate_positive_integers(self, input_list):

        self.validated_data = []  # Resetting list
        
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                self.validated_data.append(int(item))
        
        return self.validated_data

    def display_validation_message(self):
        """Displaying a message saying what happened"""
        if self.validated_data:
            print(f"valid data: {self.validated_data}")
        else:
            print("no positive integers found")
