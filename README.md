# terradoc
Generate documentation from your terraform.tfstate files.
This tool is used when you have multiples terraform.tfstate file and uses modules. It will allow to generate multiple markdown document for your developers.

## How to run

### Step 1: Add proper output parameters into your terraform.tfstate files
Each of your terraform.tfstate files should contains the following output:

#### terradoc_content
Content of the terradoc documentation, one variable as a text.

#### terradoc_title
Title of this part.

#### category_X
X being a positive number. Starts at 0, each subcontent indicates a new category
For instance:
category_0: myaccount1, myaccount2, etc.
category_1: eu-central-1, us-east-2, etc.

#### 


### Step 2: download all your terraform.tfstate file locally.

Right now, only local files are supported.

### Step 3: execute docker with your terraform.tfstate file mounted at a specified location

docker run -e "CONFIGURATION_TYPE=environment" -e "TFSTATE_LOCATION=/tmp/mytfstatefiles" -e "OUTPUT_FILE=/tmp/output" -t lysimon/terradoc:latest 
