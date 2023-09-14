seconds = int(input("What is the ammount of seconds:"));

hour = seconds // 3600;
min = (seconds // 60) % 60;
rem_seconds = seconds % 60;

print("the seconds provided equal to\n", hour, ("hours\n"), min, ("minutes\n"), rem_seconds, ("seconds"));