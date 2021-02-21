# Easy madlibs to use. You can choose any type of sentence you want. This is just example.
# Using formatted string to concatenate.

# Variables To take an input to use on runtime
adj = input("Adjective: ")
plural_noun = input("Plural noun: ")
plural_noun2 = input("Plural noun: ")
silly_word = input("Silly word: ")
type_of_liquid = input("Type of liquid: ")
adj2 = input("Adjective: ")
noun = input("Noun: ")
verb = input("Verb: ")
plural_noun3 = input("Plural noun: ")
verb_ending_in_ing = input("Verb ending in 'ing': ")
a_number = int(input("A number: "))
verb_ending_in_ing2 = input("Verb ending in 'ing': ")
plural_noun4 = input("Plural noun: ")
noun_2 = input("Noun: ")


madlibs = f"American children are fascinated by {adj} stuff \
like stories that scare the {plural_noun} off them or make their {plural_noun2} \
stand on end.Scientists say this is because being frightened causes \
the {silly_word} gland to function and puts {type_of_liquid} into \
their blood. And everyone knows that makes kids feel {adj2}. When they \
are scared by a movie or a/an {noun}.Boys laugh and holler and {verb}.\
But girls cover their eyes with their {plural_noun3} and keep screaming \
and {verb_ending_in_ing}. Most kids get over this by the time they are \
{a_number} years old. Then they like movies about cars {verb_ending_in_ing2} \
or cops shooting {plural_noun4} or, if they are girls, they like movies \
about a boy meeting a/an {noun_2} and falling in love. Ofcourse, that \
can be scary, too."


print(madlibs)

