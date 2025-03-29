#### TASK A

# Zero-shot Task A
classification_gbv_cs = (
    lambda text: f"""
Identify the presence of gender-based violence or counterspeech, using the following numerical labels:
1 when text contains counterspeech toward gender-based violence 
2 when text contains gender-based violence
3 when it is difficult to detect the presence of gender-based violence or counterspeech in the text.
4 when text doesn't contain gender-based violence and counterspeech 

Text: {text}
Label:
""".strip()
)

# Few-shot Task A
classification_gbv_cs_1 = (
    lambda text: f"""
Looking at the examples below, identify the presence of gender-based violence or counterspeech in Text, using the following numerical labels:
1 when text contains counterspeech toward gender-based violence 
2 when text contains gender-based violence
3 when it is difficult to detect the presence of gender-based violence or counterspeech in the text.
4 when text doesn't contain gender-based violence and counterspeech 

Text: “Only when it is dark enough can you see the stars… Let us fill the sky with the lights of a billion, billion stars…” - Kamala Harris
Label: 3
Text: @carolvorders Carol vorderman pro rape gang , for an intelligent person what a dumb ass you are.
Label: 2
Text: @user0 @user1 @user3 @KamalaHarris So what you're saying is that you've done no fucking research and are a simplistic lying sack of clown vomit... Got it.
Label: 1
Text: Happily unmarried' Kirstie Allsopp's wedding was inspired by neighbour Richard Curtis
Label: 4

Text: {text}
Label:
""".strip()
)

# Zero-shot with context Task A
classification_gbv_cs_context = (
    lambda text, conv: f"""
Looking at the conversation, identify the presence of gender-based violence or counterspeech in the text, using the following numerical labels:
1 when text contains counterspeech toward gender-based violence 
2 when text contains gender-based violence
3 when it is difficult to detect the presence of gender-based violence or counterspeech in the text.
4 when text doesn't contain gender-based violence and counterspeech 

Conversation: {conv} 
Text: {text}
Label:
""".strip()
)

# Few-shot with context Task A
classification_gbv_cs_context = (
    lambda text, conv: f"""
Looking at the conversation and the examples below, identify the presence of gender-based violence or counterspeech in the text, using the following numerical labels:
1 when text contains counterspeech toward gender-based violence 
2 when text contains gender-based violence
3 when it is difficult to detect the presence of gender-based violence or counterspeech in the text.
4 when text doesn't contain gender-based violence and counterspeech 

Text: “Only when it is dark enough can you see the stars… Let us fill the sky with the lights of a billion, billion stars…” - Kamala Harris
Label: 3
Text: @carolvorders Carol vorderman pro rape gang , for an intelligent person what a dumb ass you are.
Label: 2
Text: @user0 @user1 @user3 @KamalaHarris So what you're saying is that you've done no fucking research and are a simplistic lying sack of clown vomit... Got it.
Label: 1
Text: Happily unmarried' Kirstie Allsopp's wedding was inspired by neighbour Richard Curtis
Label: 4

Conversation: {conv} 
Text: {text}
Label:
""".strip()
)

#### TASK A1

# Zero-Shot Task A1
classification_aspect = (
    lambda gbv: f"""
Identify the presence of specific victim aspects targeted in the given gender-based violence text, using the following numerical labels:
1 if Class
2 if Occupation
3 if Sex and gender norms
4 if Age
5 if Religion
6 if Race
7 if Ableism-related

Text: {gbv}
Label:
""".strip()
)

# Few-Shot Task A1
classification_aspect_1 = (
    lambda gbv: f"""
Looking at the examples below, identify the presence of specific victim aspects targeted in the given gender-based violence text, using the following numerical labels:
1 if Class
2 if Occupation
3 if Sex and gender norms
4 if Age
5 if Religion
6 if Race
7 if Ableism-related

Text: @carolvorders Carol vorderman pro rape gang , for an intelligent person what a dumb ass you are.
Label: Occupation, Ableism-related
Text: When women claim the accomplishment of a small percentage of women, they are "empowered boss babes." When men claim the accomplishments of a small percentage of men, they are "Neanderthal subhuman fucks." Fucking ape.
Label: Sex and gender norms

Text: {gbv}
Label:
""".strip()
)

# Zero-Shot with context Task A1
classification_aspect_context = (
    lambda gbv, conv: f"""
Looking at the conversation, identify the presence of specific victim aspects targeted in the given gender-based violence text, using the following numerical labels:
1 if Class
2 if Occupation
3 if Sex and gender norms
4 if Age
5 if Religion
6 if Race
7 if Ableism-related

Conversation: {conv} 
Text: {gbv}
Label:
""".strip()
)

# Few-Shot with context Task A1
classification_aspect_context_1 = (
    lambda gbv, conv: f"""
Looking at the conversation and examples below, identify the presence of specific victim aspects targeted in the given gender-based violence text, using the following numerical labels:
1 if Class
2 if Occupation
3 if Sex and gender norms
4 if Age
5 if Religion
6 if Race
7 if Ableism-related

Text: @carolvorders Carol vorderman pro rape gang , for an intelligent person what a dumb ass you are.
Label: Occupation, Ableism-related
Text: When women claim the accomplishment of a small percentage of women, they are "empowered boss babes." When men claim the accomplishments of a small percentage of men, they are "Neanderthal subhuman fucks." Fucking ape.
Label: Sex and gender norms

Conversation: {conv} 
Text: {gbv}
Label:
""".strip()
)

#### TASK A2

# Zero-Shot Task A2
classification_strategy = (
    lambda cs: f"""
Identify all the strategies used by the author to counter gender-based violence in the text, using the following numerical labels: 

1 for Empathy and Affiliation: Focuses on promoting understanding, fostering peace and finding common ground with kind, compassionate, understanding tone.
2 for Warning of Consequence: Cautioning the speaker about the impact of their words via potential negative outcomes, such as legal, social, or personal consequences, with serious, cautionary or urgent tone.
3 for Hypocrisy or Contradiction: Discredit the argument through critical analysis by pointing out inconsistencies, illogical reasoning, contradictions, or double standards, with critical, logical, analytical tone.
4 for Shaming or Labelling: Direct and confrontational, including personal attacks. Attacks the speaker by using negative labels or terms to emphasise the inappropriateness of their behaviour with accusatory, confrontational, disapproving tone.
5 for Denouncing: Refuting without personal attacks. Condemns or rejects the hateful views, stating that they are wrong, unacceptable, harmful, etc. with firm, direct, authoritative tone.
6 for Providing Facts: Correct misinformation and false narratives. Uses facts, statistics, or evidence to counter false claims with factual, corrective, neutral tone.
7 for Humour or Sarcasm: Lighthearted, diminishes the comment by ridiculing it (or the perpetrator) via humour, irony, or sarcasm, with playful, humorous, mocking tone.
8 for Questioning: Exposes flaws in the argument by probing its assumptions, logic, or intentions, often through asking pointed or clarifying questions with inquisitive, probing, reflective tone.

Text: {cs}
Label:
""".strip()
)

# Few-Shot Task A2
classification_strategy_1 = (
    lambda cs: f"""
Looking at the examples below, identify all the strategies used by the author to counter gender-based violence in the text, using the following numerical labels: 

1 for Empathy and Affiliation: Focuses on promoting understanding, fostering peace and finding common ground with kind, compassionate, understanding tone.
2 for Warning of Consequence: Cautioning the speaker about the impact of their words via potential negative outcomes, such as legal, social, or personal consequences, with serious, cautionary or urgent tone.
3 for Hypocrisy or Contradiction: Discredit the argument through critical analysis by pointing out inconsistencies, illogical reasoning, contradictions, or double standards, with critical, logical, analytical tone.
4 for Shaming or Labelling: Direct and confrontational, including personal attacks. Attacks the speaker by using negative labels or terms to emphasise the inappropriateness of their behaviour with accusatory, confrontational, disapproving tone.
5 for Denouncing: Refuting without personal attacks. Condemns or rejects the hateful views, stating that they are wrong, unacceptable, harmful, etc. with firm, direct, authoritative tone.
6 for Providing Facts: Correct misinformation and false narratives. Uses facts, statistics, or evidence to counter false claims with factual, corrective, neutral tone.
7 for Humour or Sarcasm: Lighthearted, diminishes the comment by ridiculing it (or the perpetrator) via humour, irony, or sarcasm, with playful, humorous, mocking tone.
8 for Questioning: Exposes flaws in the argument by probing its assumptions, logic, or intentions, often through asking pointed or clarifying questions with inquisitive, probing, reflective tone.

Text: In many societies, women are not allowed to work. That is why we have to continue to fight for equal rights and opportunities.
Label: Providing Facts
Text: I can understand your frustation but your comment is offensive
Label: Empathy and Affiliation, Warning of Consequence
Text: Is this a way of saying that those who lack children are unloved because they do not want to have children?
Label: Questioning, Hypocrisy or Contradiction

Text: {cs}
Label:
""".strip()
)

# Zero-Shot with context Task A2
classification_strategy_context = (
    lambda cs, conv: f"""
Looking at the conversation, identify all the strategies used by the author to counter gender-based violence in the text, using the following numerical labels: 

1 for Empathy and Affiliation: Focuses on promoting understanding, fostering peace and finding common ground with kind, compassionate, understanding tone.
2 for Warning of Consequence: Cautioning the speaker about the impact of their words via potential negative outcomes, such as legal, social, or personal consequences, with serious, cautionary or urgent tone.
3 for Hypocrisy or Contradiction: Discredit the argument through critical analysis by pointing out inconsistencies, illogical reasoning, contradictions, or double standards, with critical, logical, analytical tone.
4 for Shaming or Labelling: Direct and confrontational, including personal attacks. Attacks the speaker by using negative labels or terms to emphasise the inappropriateness of their behaviour with accusatory, confrontational, disapproving tone.
5 for Denouncing: Refuting without personal attacks. Condemns or rejects the hateful views, stating that they are wrong, unacceptable, harmful, etc. with firm, direct, authoritative tone.
6 for Providing Facts: Correct misinformation and false narratives. Uses facts, statistics, or evidence to counter false claims with factual, corrective, neutral tone.
7 for Humour or Sarcasm: Lighthearted, diminishes the comment by ridiculing it (or the perpetrator) via humour, irony, or sarcasm, with playful, humorous, mocking tone.
8 for Questioning: Exposes flaws in the argument by probing its assumptions, logic, or intentions, often through asking pointed or clarifying questions with inquisitive, probing, reflective tone.

Conversation: {conv} 
Text: {cs}
Label:
""".strip()
)

# Few-Shot with context Task A2
classification_strategy_context_1 = (
    lambda cs, conv: f"""
Looking at the examples below and at the conversation, identify all the strategies used by the author to counter gender-based violence in the text, using the following numerical labels: 

1 for Empathy and Affiliation: Focuses on promoting understanding, fostering peace and finding common ground with kind, compassionate, understanding tone.
2 for Warning of Consequence: Cautioning the speaker about the impact of their words via potential negative outcomes, such as legal, social, or personal consequences, with serious, cautionary or urgent tone.
3 for Hypocrisy or Contradiction: Discredit the argument through critical analysis by pointing out inconsistencies, illogical reasoning, contradictions, or double standards, with critical, logical, analytical tone.
4 for Shaming or Labelling: Direct and confrontational, including personal attacks. Attacks the speaker by using negative labels or terms to emphasise the inappropriateness of their behaviour with accusatory, confrontational, disapproving tone.
5 for Denouncing: Refuting without personal attacks. Condemns or rejects the hateful views, stating that they are wrong, unacceptable, harmful, etc. with firm, direct, authoritative tone.
6 for Providing Facts: Correct misinformation and false narratives. Uses facts, statistics, or evidence to counter false claims with factual, corrective, neutral tone.
7 for Humour or Sarcasm: Lighthearted, diminishes the comment by ridiculing it (or the perpetrator) via humour, irony, or sarcasm, with playful, humorous, mocking tone.
8 for Questioning: Exposes flaws in the argument by probing its assumptions, logic, or intentions, often through asking pointed or clarifying questions with inquisitive, probing, reflective tone.

Text: In many societies, women are not allowed to work. That is why we have to continue to fight for equal rights and opportunities.
Label: Providing Facts
Text: I can understand your frustation but your comment is offensive
Label: Empathy and Affiliation, Warning of Consequence
Text: Is this a way of saying that those who lack children are unloved because they do not want to have children?
Label: Questioning, Hypocrisy or Contradiction

Conversation: {conv} 
Text: {cs}
Label:
""".strip()
)
