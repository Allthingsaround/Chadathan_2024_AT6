from UserInputValidator import UserInputValidator 

# 1st instance
validator1 = UserInputValidator()
inputs1 = ["10", "1000", "test", "11", "-1", "100"]
validated_data1 = validator1.validate_positive_integers(inputs1)

# 2nd
print("Instance 1 - Validated Positive Integers:")
print(validated_data1)
validator1.display_validation_message()

# create 2nd instance of method
validator2 = UserInputValidator()
inputs2 = ["1", "200", "hi", "-100", "300"]
validated_data2 = validator2.validate_positive_integers(inputs2)

# display for 2nd
print("\nInstance 2 - Validated Positive Integers:")
print(validated_data2)
validator2.display_validation_message()

