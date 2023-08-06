{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b7d17e5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intel MKL WARNING: Support of Intel(R) Streaming SIMD Extensions 4.2 (Intel(R) SSE4.2) enabled only processors has been deprecated. Intel oneAPI Math Kernel Library 2025.0 will require Intel(R) Advanced Vector Extensions (Intel(R) AVX) instructions.\n",
      "Intel MKL WARNING: Support of Intel(R) Streaming SIMD Extensions 4.2 (Intel(R) SSE4.2) enabled only processors has been deprecated. Intel oneAPI Math Kernel Library 2025.0 will require Intel(R) Advanced Vector Extensions (Intel(R) AVX) instructions.\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk import pos_tag\n",
    "from collections import defaultdict\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0c9f33f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "K1 = []\n",
    "K2 = []\n",
    "Q = []\n",
    "size = 20\n",
    "\n",
    "class POS_Analysis :\n",
    "    def __init__(self, text) :\n",
    "        self.pos = pos_tag(word_tokenize(text)) # 1. tag the part-of-speech (POS) of each word\n",
    "        \n",
    "    # allow the user to select any word or string and display the word or string in context\n",
    "    def select_word(self, word) :\n",
    "        index = [i for i, x in enumerate(self.pos) if x[0] == word]\n",
    "        lst = []\n",
    "\n",
    "        for i in index :\n",
    "            if i < 1 :\n",
    "                lst.append(self.pos[i][0] + ' ' + self.pos[i+1][0])\n",
    "            elif i > len(self.pos)-2 :\n",
    "                lst.append(self.pos[i-1][0] + ' ' + self.pos[i][0])\n",
    "            else :\n",
    "                lst.append(self.pos[i-1][0] + ' ' + self.pos[i][0] + ' ' + self.pos[i+1][0])\n",
    "            \n",
    "        return lst\n",
    "        \n",
    "    # allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
    "    def target_word(self, word) :\n",
    "        index = [i for i, x in enumerate(self.pos) if x[0] == word]\n",
    "        lst = []\n",
    "        \n",
    "        for i in index :\n",
    "            lst.append(self.pos[i][0] + ' ' + self.pos[i+1][1])\n",
    "            \n",
    "        return lst\n",
    "        \n",
    "    # count the number of identical POS patterns in each dataset\n",
    "    def count_pos(self) :\n",
    "        #print('4. count the number of identical POS patterns in each dataset')\n",
    "        d = defaultdict(int)\n",
    "        \n",
    "        for i in range(len(self.pos)-1) :\n",
    "            d[self.pos[i][0] + ' ' + self.pos[i+1][1]] += 1\n",
    "            \n",
    "        return d\n",
    "        \n",
    "    def data_print(self) :\n",
    "        print(self.pos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1bf4c2b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# allow the user to select any word or string and display the word or string in context\n",
    "def select_word() :\n",
    "    word = input('検索する単語')\n",
    "    d = defaultdict(int)\n",
    "    \n",
    "    for i in range(len(K1)) :\n",
    "        lst = K1[i].select_word(word)\n",
    "    \n",
    "        for j in lst :\n",
    "            d[j] += 1\n",
    "            \n",
    "    for i in range(len(K2)) :\n",
    "        lst = K2[i].select_word(word)\n",
    "    \n",
    "        for j in lst :\n",
    "            d[j] += 1\n",
    "            \n",
    "    for i in range(len(Q)) :\n",
    "        lst = Q[i].select_word(word)\n",
    "    \n",
    "        for j in lst :\n",
    "            d[j] += 1\n",
    "            \n",
    "    for i, j in d.items() :\n",
    "        print(i)\n",
    "        \n",
    "# allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
    "def target_word() :\n",
    "    word = input('検索する単語')\n",
    "    d = defaultdict(int)\n",
    "    \n",
    "    for i in range(len(K1)) :\n",
    "        lst = K1[i].target_word(word)\n",
    "    \n",
    "        for j in lst :\n",
    "            d[j] += 1\n",
    "            \n",
    "    for i in range(len(K2)) :\n",
    "        lst = K2[i].target_word(word)\n",
    "    \n",
    "        for j in lst :\n",
    "            d[j] += 1\n",
    "            \n",
    "    for i in range(len(Q)) :\n",
    "        lst = Q[i].target_word(word)\n",
    "    \n",
    "        for j in lst :\n",
    "            d[j] += 1\n",
    "            \n",
    "    for i, j in d.items() :\n",
    "        print(i)\n",
    "        \n",
    "# Compare the top 20 patterns\n",
    "def comp(A, B) :\n",
    "    num = 0\n",
    "    \n",
    "    for i in range(size) :\n",
    "        for j in range(size) :\n",
    "            if A[i][0] == B[j][0] :\n",
    "                num += 1\n",
    "    \n",
    "    return num\n",
    "\n",
    "# count the number of identical POS patterns in each dataset\n",
    "def analysis() :\n",
    "    K1_data = defaultdict(int)\n",
    "    K2_data = defaultdict(int)\n",
    "    Q_data = defaultdict(int)\n",
    "    K1_list = []\n",
    "    K2_list = []\n",
    "    Q_list = []\n",
    "    \n",
    "    for i in range(len(K1)) :\n",
    "        d = K1[i].count_pos()\n",
    "        for p, n in d.items() :\n",
    "            K1_data[p] += n\n",
    "            \n",
    "    for i,j in K1_data.items() :\n",
    "        K1_list.append([i, j])\n",
    "        \n",
    "    K1_list.sort(reverse=True, key=lambda x:x[1])\n",
    "        \n",
    "    for i in range(len(K2)) :\n",
    "        d = K2[i].count_pos()\n",
    "        for p, n in d.items() :\n",
    "            K2_data[p] += n\n",
    "            \n",
    "    for i,j in K2_data.items() :\n",
    "        K2_list.append([i, j])\n",
    "        \n",
    "    K2_list.sort(reverse=True, key=lambda x:x[1])\n",
    "        \n",
    "    for i in range(len(Q)) :\n",
    "        d = Q[i].count_pos()\n",
    "        for p, n in d.items() :\n",
    "            Q_data[p] += n\n",
    "            \n",
    "    for i,j in Q_data.items() :\n",
    "        Q_list.append([i, j])\n",
    "        \n",
    "    Q_list.sort(reverse=True, key=lambda x:x[1])\n",
    "    \n",
    "    while True :\n",
    "        K1_cnt = comp(Q_list, K1_list)\n",
    "        K2_cnt = comp(Q_list, K2_list)\n",
    "        \n",
    "        if K1_cnt > K2_cnt :\n",
    "            print(\"K2 is the least similar dataset.\")\n",
    "            break\n",
    "        elif K1_cnt < K2_cnt :\n",
    "            print(\"K1 is the least similar dataset.\")\n",
    "            break\n",
    "        else :\n",
    "            size += 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a36318c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------------------------------------------------\n",
      "0 : Finish and count the number of identical POS patterns in each dataset\n",
      "1 : Allow the user to select any word or string and display the word or string in context\n",
      "2 : Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
      "1\n",
      "Allow the user to select any word or string and display the word or string in context\n",
      "検索する単語to\n",
      "insights to how\n",
      "relationships to the\n",
      "is to investigate\n",
      "thought to be\n",
      "relationships to precursors\n",
      "contribute to musicology\n",
      "try to discover\n",
      "as to bridge\n",
      "According to Nattiez\n",
      "up to modern\n",
      "freedom to support\n",
      "corresponds to the\n",
      "approaches to music\n",
      "fit to the\n",
      "seem to be\n",
      "adequate to the\n",
      "us to clearly\n",
      "enough to recognize\n",
      "similarly to an\n",
      "up to chapters\n",
      "contributing to SPEAC\n",
      "assigned to groups\n",
      "approach to model\n",
      "respect to recent\n",
      "Due to a\n",
      "contrast to a\n",
      "not to teach\n",
      "AI to create\n",
      "but to be\n",
      "able to help\n",
      "belong to the\n",
      "According to the\n",
      "influence to Tchaikovsky\n",
      "us to automatically\n",
      "desire to overcome\n",
      "appeal to future\n",
      "preferred to hide\n",
      "expect to find\n",
      "possibility to incorporate\n",
      "approaches to reducing\n",
      "is to increase\n",
      "up to 110\n",
      "exposure to high\n",
      "up to 200\n",
      "due to the\n",
      "leading to a\n",
      "up to 40\n",
      ", to increase\n",
      "is to raise\n",
      "up to the\n",
      "aspect to be\n",
      "up to 80\n",
      "owing to the\n",
      "up to 105\n",
      "up to 120\n",
      "exposure to 90\n",
      "used to implement\n",
      "up to 172\n",
      "according to a\n",
      "attached to the\n",
      "density to realize\n",
      "leads to a\n",
      "leads to an\n",
      ", to further\n",
      "performed to remove\n",
      "due to incomplete\n",
      "used to fabricate\n",
      "structured to be\n",
      "designed to be\n",
      "contrast to crystalline\n",
      "leading to negligible\n",
      "them to enable\n",
      "presumed to be\n",
      "addition to the\n",
      "according to the\n",
      "polymer to the\n",
      "proportional to the\n",
      "Up to 200\n",
      "lead to a\n",
      "method to increase\n",
      "deployed to drive\n",
      "Gbaud to 56\n",
      "up to 112\n",
      "up to BER\n",
      "helpful to further\n",
      "addition to ultra-fast\n",
      "converges to a\n",
      "order to further\n",
      "effective to measure\n",
      "exposure to elevated\n",
      "contrast to previous\n",
      "time to our\n",
      "°C to 110\n",
      "sensitive to ambient\n",
      "corresponding to the\n",
      "down to room\n",
      "attributed to the\n",
      "exposure to a\n",
      "up to 110-5\n",
      "respect to the\n",
      "sensitivity to ambient\n",
      "approaches to overcome\n",
      "corresponding to higher\n",
      "comparison to other\n",
      "addition to decreasing\n",
      "up to 90\n",
      "subject to high\n",
      "solution to ensure\n",
      "footprint to sub-millimeter\n",
      "optimized to realize\n",
      "interconnects to facilitate\n",
      "material to counterbalance\n",
      "materials to effective\n",
      "vacuum to form\n",
      "cladding to protect\n",
      "polymer to align\n",
      "device to room\n",
      "matched to the\n",
      "used to characterize\n",
      "limited to 70\n",
      "fed to the\n",
      "down-sampling to form\n",
      "fed to a\n",
      ", to alter\n",
      ", to perform\n",
      "activated to verify\n",
      "aspects to be\n",
      "them to manage\n",
      "help to overcome\n",
      "individuals to memorize\n",
      "approach to link\n",
      "context to a\n",
      "action to be\n",
      "confirmations to the\n",
      "linked to location\n",
      "go to find\n",
      "helpful to be\n",
      "helpful to describe\n",
      "like to watch\n",
      "needs to do\n",
      "linked to domain-specific\n",
      "us to refine\n",
      "connected to the\n",
      "grounds to discover\n",
      "entities to be\n",
      "assumed to belong\n",
      "are to be\n",
      "use to fa-\n",
      "assumed to be\n",
      "referring to the\n",
      "wishes to save\n",
      "scenarios to be\n",
      "actions to create\n",
      "back to the\n",
      "challenges to resolve\n",
      "is to assure\n",
      "connection to specific\n",
      "connected to some\n",
      "applications to trigger\n",
      "distancing to decide\n",
      "lead to annoying\n",
      "important to elicit\n",
      "wish to proceed\n",
      "hard to follow\n",
      "referring to a\n",
      "than to a\n",
      "activity to a\n",
      "plan to be\n",
      "sync to make\n",
      "easier to use\n",
      "services to synchronize\n",
      "shown to be\n",
      "used to recognize\n",
      "proximity to locations\n",
      "information to ensure\n",
      "need to develop\n",
      "needs to be\n",
      "tend to create\n",
      "enough to accommodate\n",
      "efforts to move\n",
      "Possibilities to apply\n",
      "that to identify\n",
      "scenario to the\n",
      "results to contrast\n",
      "--------------------------------------------------------------------------------------------\n",
      "0 : Finish and count the number of identical POS patterns in each dataset\n",
      "1 : Allow the user to select any word or string and display the word or string in context\n",
      "2 : Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
      "2\n",
      "Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
      "検索する単語to\n",
      "to WRB\n",
      "to DT\n",
      "to VB\n",
      "to NNS\n",
      "to NNP\n",
      "to JJ\n",
      "to NN\n",
      "to RB\n",
      "to VBG\n",
      "to CD\n",
      "to RBR\n",
      "to VBN\n",
      "to PRP$\n",
      "to JJR\n",
      "--------------------------------------------------------------------------------------------\n",
      "0 : Finish and count the number of identical POS patterns in each dataset\n",
      "1 : Allow the user to select any word or string and display the word or string in context\n",
      "2 : Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
      "0\n",
      "K2 is the least similar dataset.\n"
     ]
    }
   ],
   "source": [
    "def main() :\n",
    "    #text = 'The first suggestion to learn something using ChatGPT is to make quizzes.'\n",
    "    # folderのパス\n",
    "    K1_folder_path = \"K1 dataset\"\n",
    "    K2_folder_path = \"K2 dataset\"\n",
    "    Q_folder_path = \"Q dataset\"\n",
    "    \n",
    "    # folderのfileを取得\n",
    "    K1_files = os.listdir(K1_folder_path)\n",
    "    K2_files = os.listdir(K2_folder_path)\n",
    "    Q_files = os.listdir(Q_folder_path)\n",
    "    \n",
    "    # dataset K1\n",
    "    for file in K1_files :\n",
    "        if file.endswith(\".txt\") :\n",
    "            file_path = os.path.join(K1_folder_path, file)\n",
    "            f = open(file_path, 'r')\n",
    "            text = f.read()\n",
    "            K1.append(POS_Analysis(text))\n",
    "            \n",
    "    # dataset K2\n",
    "    for file in K2_files :\n",
    "        if file.endswith(\".txt\") :\n",
    "            file_path = os.path.join(K2_folder_path, file)\n",
    "            f = open(file_path, 'r')\n",
    "            text = f.read()\n",
    "            K2.append(POS_Analysis(text))\n",
    "            \n",
    "    # dataset Q\n",
    "    for file in Q_files :\n",
    "        if file.endswith(\".txt\") :\n",
    "            file_path = os.path.join(Q_folder_path, file)\n",
    "            f = open(file_path, 'r')\n",
    "            text = f.read()\n",
    "            Q.append(POS_Analysis(text))\n",
    "    \n",
    "    while True :\n",
    "        print('--------------------------------------------------------------------------------------------')\n",
    "        print('0 : Finish and count the number of identical POS patterns in each dataset')\n",
    "        print('1 : Allow the user to select any word or string and display the word or string in context')\n",
    "        print('2 : Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ')\n",
    "        order = int(input())\n",
    "        \n",
    "        if order == 0 :\n",
    "            break\n",
    "        elif order == 1 :\n",
    "            # allow the user to select any word or string and display the word or string in context\n",
    "            print('Allow the user to select any word or string and display the word or string in context')\n",
    "            select_word()\n",
    "        elif order == 2 :\n",
    "            # allow the user to search for POS patterns following the target word, e.g. absolutely + JJ\n",
    "            print('Allow the user to search for POS patterns following the target word, e.g. absolutely + JJ')\n",
    "            target_word()\n",
    "        else :\n",
    "            print(str(order) + \" is nothing. Reinput from 0 to 2.\")\n",
    "            \n",
    "    # count the number of identical POS patterns in each dataset\n",
    "    analysis()\n",
    "\n",
    "if __name__ == \"__main__\" :\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}