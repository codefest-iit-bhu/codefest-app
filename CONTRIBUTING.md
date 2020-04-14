# Contributing Guidelines

Welcome, and thanks in advance for your help! Please follow these simple guidelines :+1:

## What should you know before you get started?

### Vue.js and Node.js basics

Node.js is an open source server environment which allows you to run JavaScript on the server whereas on the other hand, Vue.js is an open-source JavaScript framework for building user interfaces and single-page applications.

#### Setting up the enviornment

Often while working on various projects, you will come across situations where two projects would be running on different node versions. In such scenarios **nvm** comes to the rescue. NVM - Node Version Manager allows you to manage multiple versions of Node.js on the same machine.

- **Installing nvm :** 
    For installing nvm refer to the following link. [Link](https://github.com/nvm-sh/nvm)

- **Installing Node.js:**
    - For installing stable release of Node.js
    ```sh
    nvm install stable
    ```
    - Replace stable with a version number to install a specific version.
    - For selecting the installed version
    ```sh
    nvm use stable/version_number
    ```

- **Installing project dependancies:**
    Once done with the above steps, run the following command from the shell to install the project dependencies.
    ```sh
    npm i
    ```
    > NPM - Node Package Manager is the package manager for node. It helps with installing various packages and resolving their various dependencies.

- **Running the project:**
    ```sh
    npm run watch
    ```

Now you are ready to rock !!! 
But wait, let us introduce you to the project structure first.

### Project Structure

The __src__ directory contains the source code of the project. In this directory you will find various directories :

- **assets** : This directory stores all the images, vector graphics, and other assets that are used in the project.
- **components** : Every complex webpage consists of various simple components. These simple components are combined together to make individual pages. This directory contains the components which have been used in various pages.
- **pages** : Each page is also a component which uses other components to create the complete structure of the page. This directory consists of webpage components.
- **router** : This directory contains a file that is responsible for the routing of webpages.
- **styles** : Consists of stylus files, which define globally defines styling variables, animations, fonts, mixins, etc.
- **js & store** : As the name suggests, these directory contains js scripts, used in the project. These files define constants, exceptions, terminal commands, etc.

## How to contribute to CodeFest19-Website?

### When you propose a bug fix

**Note:** Please make sure to write an issue first and get enough feedback before jumping into a Pull Request!

- Please make sure there is an open issue discussing the new feature or bug fix.
- If there isn't, please open an issue so we can talk about it before you invest time into the implementation
- When creating an issue, follow the following guidelines:
    - Keep the title descriptive, and at the same time, it must not be too long.
    - Describe the bug fix and if possible attach a screenshot of the same.

### When you want to work on an existing issue

**Note:** Please write a quick comment in the corresponding issue and ask if the feature is still relevant and that you want to jump into the implementation.

We will do our best to respond/review/merge your PR according to priority. We hope that you stay engaged with us during this period. 


#### General Guidelines

**Note:** Don't clone the original repository directly.

1. **Fork:** Create a fork of the original repository.
2. **Clone:** Clone the forked repository to your local machine.
3. **Install:** Install the project dependencies.
4. **Branch and Work:**(Preferable) Create a new branch and work on that branch.
5. **Merge and Push:** Once done, merge your changes to the frontend branch and push the changes to the forked repository.
6. **Create a PR:** Make a pull request to the original repository (include the link of the issue resolved by this PR ).
