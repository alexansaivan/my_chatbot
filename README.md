# dialogov

## Overview

**dialogov** is an interactive assistant designed designed to assist users with issues related to official government processes. It focuses on providing information and guidance in areas such as authorizations, document validity checks, and general inquiries, all sourced from the [official Greek government page](https://www.gov.gr/en/) in English. The chatbot is built using Rasa, incorporating natural language understanding to simplify user interactions.

## Domain

The chosen domain for **dialogov** focuses on addressing common user needs related to official government procedures. Users can seek assistance in areas such as authorizations for specific actions, obtaining birth certificates, checking the validity of documents, and more. The chatbot ensures transparency and credibility by sourcing information directly from the official Greek government page in Englih [https://www.gov.gr/en/](https://www.gov.gr/en/).

## Intention

The primary intention behind developing **dialogov** is to create a versatile and user-friendly conversational interface. By leveraging natural language understanding, the chatbot simplifies complex government processes, enhances accessibility, and makes it easier for users to obtain essential information from the official government source.

## Scenarios

### Happy Path 1

1. User initiates a greeting.
2. User agrees to continue.
3. User requests authorization information.
4. Chatbot provides details on authorizations with references to the official government page [here](https://www.gov.gr/en/ipiresies/polites-kai-kathemerinoteta/psephiaka-eggrapha-gov-gr/ekdose-exousiodoteses).
5. User expresses gratitude.
6. User says goodbye.

### Happy Path 2

1. User greets the chatbot.
2. User agrees to continue.
3. User requests information on issuing a birth certificate.
4. Chatbot provides details on the process with references to the official government page [here](https://www.gov.gr/en/ipiresies/oikogeneia/gennese/pistopoietiko-genneses).
5. User expresses thanks.
6. User asks about checking document validity.
7. Chatbot guides the user on checking document validity.
8. User expresses gratitude.
9. User says goodbye.

### Sad Path

1. User greets the chatbot.
2. User agrees to continue.
3. User seeks information on vaccination.
4. Chatbot provides vaccination information with references to the official government page [here](https://www.gov.gr/en/ipiresies/ugeia-kai-pronoia/koronoios-covid-19/pistopoietiko-emboliasmou).
5. User denies the provided information.
6. User denies again.
7. Chatbot apologizes.
8. User says goodbye.

### Bot Challenge

1. User challenges the chatbot's identity.
2. Chatbot responds, confirming its nature as a bot.

## Desired Capabilities

dialogov is intended to have the following capabilities:

- Providing accurate and detailed information on authorizations.
- Guiding users through processes such as issuing birth certificates.
- Assisting in checking the validity of documents.

## Usage

To interact with dialogov, follow the steps outlined in the [Getting Started](#getting-started) section below.

## Getting Started

1. Install the necessary dependencies by running:

    ```bash
    pip install rasa
    ```

2. Train the Rasa model:

    ```bash
    rasa train
    ```

3. Open a new terminal window, activate the virtual environment, and initiate the Rasa shell:

    ```bash
    rasa shell
    ```

Engage in conversations and interact with dialogov directly through the command line, utilizing the trained model!
