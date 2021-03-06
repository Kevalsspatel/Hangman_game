{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMHLxWvVAt4X5+8+dYpnla4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kevalsspatel/Hangman_game/blob/master/Hangman_game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qIbvckcvj6Q1",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# setup the word and hidden list\n",
        "word = list(\"apple\")\n",
        "hidden = []\n",
        "for character in word:\n",
        "    hidden.append(\"_\")\n",
        "\n",
        "attempts = 0\n",
        "max_attempts = 4\n",
        "\n",
        "# loop until either the player has won or lost\n",
        "isGameOver = False\n",
        "while not isGameOver:\n",
        "\n",
        "    # display the current board, guessed letters, and attempts remaining\n",
        "    print(f\"You have {max_attempts - attempts} attempts remaining\")\n",
        "\n",
        "    print(f\"The current word is: {' '.join(hidden)}\")\n",
        "\n",
        "    print(\"     ------\")\n",
        "    print(\"     |    |\")\n",
        "    print(\"     |    \" + (\"O\" if attempts > 0 else \"\"))\n",
        "    print(\"     |    \" + (\"/\\\\\" if attempts > 1 else \"\"))\n",
        "    print(\"     |    \" + (\"|\" if attempts > 2 else \"\"))\n",
        "    print(\"     |    \" + (\"/\\\\\" if attempts > 3 else \"\"))\n",
        "    print(\" --------\")\n",
        "\n",
        "    # ask the player for a character\n",
        "    letterGuessed = input(\"Please guess a letter: \")\n",
        "\n",
        "    print('\\n\\n\\n\\n')\n",
        "\n",
        "    if letterGuessed in word:\n",
        "        # if the player guessed correct, show all matched letters and print message\n",
        "        print(f\"You guessed correctly! {letterGuessed} is in the word\")\n",
        "        for i in range(len(word)):\n",
        "            character = word[i]\n",
        "            if character == letterGuessed:\n",
        "                hidden[i] = word[i]\n",
        "                word[i] = \"_\"\n",
        "    else:\n",
        "        # if player guessed wrong, print failure message and increment attempts\n",
        "        print(f\"You guessed wrong! {letterGuessed} is NOT in the word\")\n",
        "        attempts += 1\n",
        "\n",
        "    # if the player has won print a win message and stop looping\n",
        "    if all(\"_\" == char for char in word):\n",
        "        print(\"Congrats, you won!\")\n",
        "        isGameOver = True\n",
        "\n",
        "    # if the player has lost, print failing and stop looping\n",
        "    if attempts >= max_attempts:\n",
        "        print(\"You lost, rest in peace!\")\n",
        "        isGameOver = True"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}