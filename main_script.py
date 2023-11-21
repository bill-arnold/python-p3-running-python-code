# main_script.py

# Read and execute the code from "lib/app.py"
fname = "lib/app.py"

with open(fname, "rU") as f:
    code = compile(f.read(), fname, 'exec')

# Now you can execute the compiled code
exec(code)

# Additional code in your main script
print("Main script continues...")
