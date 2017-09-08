# The script of the game goes in this file.

# declare images

image bg jungle-day = "jungle.png"
image bg ark = "ark.png"
image bg calypso-day = "calypso-day.png"
image bg calypso-night = "calypso-night.png"
image bg earth-day = "earth-day.png"
image bg earth-night = "earth-night.png"
image bg cliffs = "cliffs.png"
image bg space = "space.png"
image bg mountains = "mountains.png"
image bg shuttle = "shuttle.png"
image bg calypso-island = "calypso-island.png"
image bg title-page = "title-page.png"
image bg jungle-night = "jungle-night.png"
image bg black = "black.png"
image bg field-day = "field-day.png"
image bg field-night = "field-night.png"

image penelope neutral = "penelope_neutral.png"
image penelope sad = "penelope_sad.png"
image penelope angry = "penelope_angry.png"
image penelope confused = "penelope_confused.png"
image penelope happy = "penelope_happy.png"
image penelope delighted = "penelope_delighted.png"

image calypso neutral = "calypso_neutral.png"
image calypso sad = "calypso_sad.png"
image calypso shy = "calypso_shy.png"
image calypso curious = "calypso_curious.png"
image calypso happy = "calypso_happy.png"
image calypso thoughtful = "calypso_thoughtful.png"

image scout neutral = "scout_neutral.png"
image scout suspicious = "scout_suspicious.png"
image scout angry = "scout_angry.png"
image scout happy = "scout_happy.png"
image scout curious = "scout_curious.png"
image scout sad = "scout_sad.png"

image hector young neutral = "hector_youngneutral.png"
image hector young happy = "hector_younghappy.png"
image hector young sad = "hector_youngsad.png"
image hector young angry = "hector_youngangry.png"
image hector young surprised = "hector_youngsurprised.png"

image hector mid neutral = "hector_midneutral.png"
image hector mid happy = "hector_midhappy.png"
image hector mid sad = "hector_midsad.png"
image hector mid angry = "hector_midangry.png"
image hector mid surprised = "hector_midsurprised.png"

image hector old neutral = "hector_oldneutral.png"
image hector old happy = "hector_oldhappy.png"
image hector old sad = "hector_oldsad.png"
image hector old angry = "hector_oldangry.png"
image hector old surprised = "hector_oldsurprised.png"

image friend dark = "friend_dark.png"
image friend light = "friend_light.png"

image leader happy = "leader_happy.png"
image leader sad = "leader_sad.png"
image leader neutral = "leader_neutral.png"

image dad happy = "dad_happy.png"
image dad sad = "dad_sad.png"
image dad worried = "dad_worried.png"
image dad angry = "dad_angry.png"
image dad neutral = "dad_neutral.png"

image son neutral = "boy_neutral.png"
image son angry = "son_angry.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Traveller")
define p = Character("Penelope")
define c = Character("Calypso")
define com = Character("Commander")
define s = Character("Scout")
define sol = Character("Soldier")
define u = Character("Creature")
define h = Character("Hector")
define l = Character("Leader")
define w = Character("Warrior")
define d = Character("Father")
define b = Character("Son")
define g = Character("Girl")


# The game starts here.

label start:

scene bg earth-day
with fade

"I walk until I can no longer feel my feet."
"My ankles swell with the strain of my belly."
"I reach the camp."
"My feet crunch against the thick ashes of bodies. The ashes are warm. They soothe my blisters."
"I hear crying, distantly."
"I should save them."
"The fight is not easy, but I save them."
"The camp burns. Black smoke fills my lungs. My hair is heavy with soot."
"I lead the survivors from the ruins."
"They want to ask me who I am, how I got here, how I saved them. But I will not tell them."

"Instead I will lead them to what remains of our army."

"Families trip over themselves running to each other."
"I have to convince my commanding officer that I'm not a mirage."

"The survivors cry for a long time."

"I sit down and rest my legs."

"The commander vows to continue the fight."

"My belly grows bigger."

"We lose ground."
"There is talk of using the ark. We don't know if anyone else is left."

"My belly swells. I can feel her kicking, sometimes."

"We decide to use the ark."

"The commander makes the order to begin preparing to leave Earth."

"My water breaks."

scene bg earth-night

"She is beautiful."

"I name her Penelope."

"Preparations to leave the planet move slowly."
"We can’t move too many people to the ark at once - it would attract too much attention."
"So we gather food and supplies and look for stragglers."
"I know these hills better than any of the others, so I lead the search parties."

"Penelope is loud. She keeps me awake at night, crying and whining."
"The search parties are calmer than staying at camp with her."

"But she misses me when I'm gone. She looks at me sometimes, makes noises, tugs at my fingers."
"Just when I feel myself collapsing from exhaustion, she touches my nose and gurgles and I'm jolted awake with love for her."

"I am enjoying a moment of quiet, reading over supply lists in the corner of our tiny room, when I hear something rustling on the floor."

"She is on her feet, wobbling and teetering with the effort. Tentatively, she takes a step."

"And another."

"She walks to me."

"The remaining supplies are dwindling. We will have to choose whether to feed everyone here or stock up the ark."

"But I don't care."

"The supply lists flutter to the floor as I take her up in my arms."

"She is smiling, giggling, confident."

"Her first words are more like a grumble, but then they come out all at once in a matter of weeks, and before I know it she is babbling non-stop."

"I start to take her to meetings. She babbles through them as we discuss strategy."

"We have to move our west-side camps. The enemy is too close to them, and if we are discovered the whole operation would be compromised."

"I will lead the relocation."
"We will have to move through the hills."
"Even if we pass unnoticed, the road is long, steep and dangerous."
"Some of our people will die - the elderly, the sick, maybe some of the children."

"I hug Penelope more tightly than I ever have, and leave her with the commander."

"When I return, she calls me mom."

"Penelope has names for things now."
"She wants to know what everything is called, why it is the way it is, how it works."
"She asks these questions of me but also of the others."
"She asks them until they get angry and I have to apologize on her behalf."

"I take her for as many walks as I can, but the preparations are almost complete."
"I have to attend to them. I leave her alone more than I'd like."

"She comes up with her own names for things while I'm gone."
"When I come back after a hard day to find that - in a complete coincidence - she has decided to call 'bees' 'cees', I find myself laughing so hard that my sides hurt."
"She starts crying. She likes her name better. Why can't we just change it?"

"She loves when the kitchen serves stew."
"She likes to pick coriander from the garden and cover her portion in it until her bowl tastes overwhelmingly of coriander."
"She cries when we run out of coriander and I can't find any more."

"I don't want to tell her that she will never eat it again."

"We are on a walk picking flowers when explosions light up the horizon, followed by clouds of black smoke."

"I pick her up and run back to the base."

"The commander looks at me as I enter the room, and I know."

"It’s time to leave."

"Penelope won't stop crying as I pack her things."
"I go to zip up her bag but she stops me."
"She stuffs it full with the flowers from our walk."
"Then she looks at me, her eyes puffy with tears."
"I freeze in that look. All I want to do is make her happy again."

"The alarm sounds through the hallways. I can’t hear anything beyond it. I snap back to the present."

"Regulations. We have to follow the rules."
"Some of the refugees are allergic to pollen, and if too much of it were to get into the air vents--"

"I take the flowers out of the bag and scatter them on the bed."
"She cries harder, grabs them, grabs onto the sheets and then the mattress."
"She is screaming now. She won't leave."

"The alarm sounds again. We have to go."

"I take her by the waist and pull as hard as I can."
"I pull her fingers from the mattress."
"She holds on with one hand and so I drag her out the door until she can't fit the mattress and she has to let go."
"She shrieks into my ear."
"She doesn't want to leave, she doesn't want to leave, she won't leave."

"I see her blanket sprawled on the floor."
"It has little cats on it, prancing around and playing with balls of yarn."
"She's never met a cat, but she imagines that all the cats on this blanket are hers, and tosses it around to get them to play with her."
"It's probably covered in snot and drool and who knows what by now, but she cuddles up to it every night."
"I rarely have the chance to wash it because she won't sleep without it."

"The alarm sounds again. She is fighting me now."

"I hold her tightly and run for the exit."

"The doors close a few minutes after we make it in."


"The commander worries about the enemy forces."
"We are making ourselves a target as long as we idle here. We can't sacrifice ourselves for a few stragglers."

"She is right. But I look around."
"Fewer than half of us made it."
"The ark's halls are practically empty."
"Those who remain are crying, gasping, searching for families who didn't make it in."

"Penelope has stopped fighting in my arms. I get her to a chair and buckle her in next to me."

"The ark comes to life with a rumble that feels like an earthquake."

"As soon as the ground stops shaking I leap out of my chair and press my face against the glass."
"Penelope struggles with her seatbelt but finds the clip and joins me."

"We watch our home get smaller and smaller out the window."
"We see cities blackened by bombs."
"We see black specks on white fields and I know they are labour camps."
"We see smoke. Ships. Debris."
"Then we are above the clouds."
"The sky gets darker as we ascend deeper into it."
"Distantly, beyond the clouds, we see a smouldering patch of red and orange."
"Some huge tract of land, set ablaze. It must be the size of a small country."

scene bg space

"The Earth is distant now. It's about the size of an apple in the window."

"I hold Penelope close to me."

p "Is that our home?"

t "Yeah. It was."

"Everything we have known is in that tiny circle in the window."

"It gets smaller and smaller until it's smaller than the stars."

scene bg title-page
with Dissolve(2.0)

pause(2.0)

scene bg ark
with Dissolve(2.0)

"I am lost in the stars again."

"For a while, I could still pinpoint our Sun amongst them..."
"but it's been months, I think, since it faded away into the thousands of others that surround us."

"I miss home."
"I miss my walks with Penelope in the gardens."
"I miss flowers and coriander."
"And even though I promised myself I wouldn't think of it, I miss the time before Penelope, too."

"I allow myself a moment in the stars, just to think about it. To remember—"

p "Mom!"

show penelope neutral

"Penelope tugs at my arm, pulling me back to the ark. I look down at her, straining to conceal my irritation."

p "You're staring again."

"I can't help but smile at how serious she looks. She's gotten bigger these past few months, and so much more talkative. And she barely cries anymore. I'm not sure how happy I should be about that."

t "I’m sorry, Nel. It's just..."

"I grasp for something happy to tell her about."

t "You're probably used to the stars by now, but I haven't seen so many in my entire life. It still gets me sometimes."

show penelope angry

"She frowns. I can tell she sees through my words."

p "Are we gonna live on one of those stars?"

t "Not on it, near it - on a planet. But yeah. I hope so."

show penelope confused

p "Why not on the star?"

t "It's too hot to build a home there. You have to live on a planet, like we did with the Sun."

p "Can anyone live on the Sun?"

t "I don't think so."

p "Oh."

"She takes that in. It seems like a lot to think about."

show penelope neutral

p "Will we ever go back home? To the Sun and to... to our place?"

menu truth_menu:
   "She looks back up at me again. Her eyes are wide, hopeful."
   "Be honest.":
     $ truth = True
     "I sit down on the floor so she can look down at me. Her neck must be tired from looking up."
     "And she needs to hear this."

     t "No,"
     t "We won't. We have to try to find a new home."
     show penelope sad
     p "What'll happen to our place?"

     t "It's someone else's place now."

     p "Why?"

     "I open my mouth to answer, but even simple words escape me, and the past is sharp again."

     "I hug her."

     t "They took it."
     t "It's theirs now. I'd take it back if I could, but I..."
     show penelope happy
     p "Don't be sad, mom."
     "She pats my head."
     p "We'll make a home on a nicer star."

     "I have time to eke out a smile before the PA system calls my name."
     "I stand up again and take Penelope's hand, and together, we walk out into the hallway."

   "Lie.":

     $ truth = False

     "I manage a smile."

     t "You never know."

     t "It’ll probably be different by the time we get back, but someday, maybe—"
     show penelope happy

     p "Will our house still be there?"

     "I haven't seen her this excited in a while."

     t "I don't think so."

     p "What about the big moonrock?"

     t "Maybe, but unlikely..."
     p "The hills by the backyard?"

     t "Probably."

     p "We'll build our new house on top of the hills. It's nicer up there."

     "The hills were rocky and jagged, hardly suitable for building a house."

     t "Of course we will."

     p "What about the flowers?"

     "The PA calls out my name before I can answer."

     t "We shouldn't keep them waiting."

     "I take her hand. She skips next to me to the hallway, thoughts of flowers thankfully lost."

label after_menu:

hide penelope

"I’m still not used to how flat the ground is on the ark."
"For something built so quickly, it’s impressively designed."
"The floors are clean white metal, with wide arches framing views of the stars drifting by outside."
"The whole ark spins in a wide, slow circle that helps to simulate gravity, but it's hardly noticeable."
"We don’t notice the long nights, either."
"I say it’s been nine months since we left Earth, but it only feels that way."
"Actually, to conserve resources, every night when we fall asleep in our pods, the station puts us into stasis."
"We haven’t figured out how to keep a person in stasis successfully for too long, so each ‘night’ lasts approximately three weeks..."
"But I prefer not to count."
"All I know is that every morning I wake up ravenously hungry and a little disoriented,"
"And that I don’t remember any of my dreams."

if truth:
     "I tried to explain it to Penelope, but it seems to have upset her."
     "She tries not to sleep now. She throws tantrums before bed."
     "At least our stasis pod fits two. That makes it a little easier."

     jump post_truth1

else:
     "I hope that Penelope doesn’t notice..."
     "I think it would only confuse her if she knew."

label post_truth1:

"Officers salute me as I pass through the doors into the bridge."
"I nod to them. They look concerned about something."
"The bridge is dome-shaped, the entire ceiling made of glass."
"The screens on the glass depict the constellations and our rough location among them."
"Towards the ground, they cycle through text, graphs and charts showing our velocity, resources, and nearby star systems."
"The seats normally all face inward towards the center, but right now the bridge crew are focused on their own screens."
"It's a little like a planetarium - and just as dark. Penelope clutches my leg. She's still scared of it."
"I had them bring a couch in here when we came aboard, and this is where I put her, with the promise I won't take long."
"She's nervous at first, but when I set up a game to play on one of the screens while I'm gone, she settles down."
"The commander stands at the center of the room, staring at some charts at her station. Before she notices me, I see concern clouding her face - but as soon as she sees me, she hides it."
com "Your clearance came through. Congratulations, Lieutenant."
t "Thanks."
com "I've got some news you'll want to hear."
"She presses a button on her screen, and one constellation in the dome above us - one quite close to our ship - lights up."
com "We've found a cluster of star systems with planets that could be habitable."
com "We're not sure about our readings just yet, but it looks like there are at least five planets in the habitable zone."
t "How long will it take us to get to them?"
com "The first is only a few days away. The others are farther, but if we stretch the stasis systems we could get to the next one within a few months."
t "That's great..."
t "What's the catch?"
"The commander sighs heavily and stares past the dome, back into space. I wonder if she's familiar enough with the map to know which star we're going to."
com "We're not sure what it is yet, but the system is littered with debris. We'll need some people to scout the system and find a path through. Without that path, we can't get to the planet."
"I look back at Penelope. She's engrossed in her game now. She barely notices the dark."
t "I can go."
com "Are you sure? We don't have many poeple, but there are others..."
t "What are the readings on this planet?"
"The commander looks around at the other officers, then leans in close to me."
com "I don't want to get people's hopes up, but..."
"they're good. Really good. We're reading fresh water, warm temperatures, oxygen... this could be home."
t "Then of course I'll go."
com "Thank you."
com "Really."
com "The first scouting party will be leaving this evening. I understand if you want to take more time..."
t "It's alright."
"I don't want to throw off the schedule."
com "Alright."
com "I'll assign someone to take care of Penelope. If we're lucky you should only be a day or two. If you get caught up in the debris, come straight back."
com "With at least six planets within our range, we can afford to wait a few months. We have the resources."
t "I understand, commander. I'll be careful."
com "Be safe, lieutenant. I'll have the scouting ship prepared for you."
"I return to Penelope. It's good timing - she's almost defeated the boss."
"She doesn't seem to notice me. Her fingers type out an angry rhythm of attacks, each of which causes the boss to flinch."
"Finally, he dies in an explosion of blues and purples. Penelope pumps her fists in the air."
show penelope delighted
p "Did you see that?!"
t "I did! Nice work!"
p "Did you see that it was hard mode?"
"I raise my eyebrows."
t "Really?"
"She nods vigorously."
"I haven't beaten that boss in hard mode."
t "Guh... good job!"
"She still has this ridiculous grin on her face as we walk down the hallway."
"I want to tell her about my mission, but she's chattering on about the game."
p "And then I used the rolling attack, only I jumped behind him so he couldn't get me."
t "That's a great strategy."
"I swear I tried that."
"We reach our room again."
show penelope happy
p "And so... and so then he died."
p "And I got the big treasure chest."
p "I haven't opened it though."
t "I'm sure it'll be something great."
p "I think it's the bow, right?"
p "I really like the bow."
p "I'm really good at shooting stuff."
t "Penelope..."
show penelope neutral
p "Do you wanna play together tonight?"
t "I... I can't. I'm sorry."
show penelope sad
p "How long will you be gone?"
if truth:
    t "I'm not sure yet."
    jump post_truth2
else:
    t "I shouldn't be more than a week."
    "I hope it's not more than a week."
label post_truth2:
p "Can we play when you get back?"
t "Of course. And you know..."
t "We might even be playing on a new planet, if my mission goes well."
show penelope neutral
p "Really?"
p "What kind of planet? Is it warm? Are there flowers? Will it have coriander?"
t "...We'll just have to wait and see, won't we?"
p "Okay."
"I remember the flowers we left on Earth. The regulations. I ruffle Penelope's hair."
t "If I can find a flower, I'll bring one back for you."
show penelope happy
p "Promise?"
t "I promise."
"Regulations be damned."
hide penelope

scene bg shuttle

sol "All preparations complete, Commander."
t "Thank you."
"The shuttle whirs to life. A hatch opens on top of it."
"It seats one, with barely enough room to stretch out your arms. The first time I flew it, I felt so claustrophobic I had trouble focusing."
"Now, after so long in the emptiness of the ark, it's almost comforting."
"I sit down in the cockpit and close the hatch above me."
"When it's closed, the hatch forms a clear glass dome - almost a miniature of the bridge."
"I press my fingertips on the controllers on the arms of the chair and the screens lining the dome come to life."
"I check the energy levels, shields, the stasis pod. All in working order."
"I open the map. The tiny red dot is the ark; the yellow one, smaller and flashing, is me."
"I turn on the antimatter engine. It makes a low hum - I can almost feel the buzzing in my seat."
"The hangar door opens. I turn on the radio."
sol "Have a safe trip."
t "I'll try. Don't have too much fun without me."
"I push forward with my fingertips. The ship buzzes again, and with a jolt the shuttle pushes out into space."
"I look at the windows as I fly past the ark. A few people have lined up to watch me go."
"I wonder where Penelope is among them."
"I think I see a smaller shadow among the group -"
"...but the shuttle finds its course and accelerates."
"The ark fades into the vaccuum of space."
"I turn my attention to the screens. Everything looks stable."
"The shuttle has plotted a course, and the autopilot is working properly."
"I could go into stasis now, but I play Penelope's game for a couple of hours first."
"I still can't beat that boss."
"More exhausted than frustrated, I give up and look out at the stars for a while."
"If I turn down the lights inside the ship, they're so bright that it's almost dizzying."
"I really haven't seen this many stars in my life."
"I make one last check - all systems running smoothly - and turn on the stasis pod."
"The chair reclines backward until it lies flat. The control panel on the armrest opens up; I slip my arms inside of it and it closes around them."
"I feel a sting in my wrists - the needles going in. But before I really feel it, my body starts to relax."
"I try to stare up out the window a moment longer, but sleep takes me before I realized that my eyes are already closed."

scene bg black
with Dissolve(2.0)

pause(3.0)

"Stasis is dreamless and timeless."

scene bg shuttle
with Dissolve(0.5)

"I am awoken by a jolt."

"A second later, the blaring, overwhelming sound of an alarm fills my ears."
"Needles still in my arms, I press my hands down into the control panels and pull my seat back up."
"The alarm makes my head hurt."
"I press buttons until it turns off."

"My ears still ringing, I check the screens."
"The shields have taken a hit. They're dangerously low."
"I ping the ark, but there's no answer."
"I look up out the window and see why."
"All I see in every direction as far as I look is debris. There are asteroids the size of small moons--"
"But more worryingly, there are thousands upon thousands of smaller ones. Even something half a meter long could destroy the shuttle."
"As I scan the debris I start to see other things, too - dark metal carved into smooth curves, broken wires as wide as me, the broken remains of what looks like a room."
"Other ships have found their end here."
"There's no way the ark could make it through."
"I need to get back and deliver the bad news."
"I bring the ship about - and my heart sinks."
"I'm in the middle of the field."
"I'm jolted again, and just as I come back to my senses the alarm starts back up."
"I go to turn it off - and look up to see a massive rock directly in my path."
"I turn the auto-pilot off, rev the engines and pull up as hard as I can."
"I barely skate over the asteroid - and into the path of another."
"I swerve to the right and downwards and then left again."
"My shields are at 40 percent."
"I look at the map, then frantically out the window..."
"And I see it: a small bluish circle."
"The planet. Perhaps the debris will be lighter there, and I can send a signal--"
"The shuttle shakes with another impact."
"Shields at 22 percent."
"I accelerate towards the planet and away from the rock."
"I push the engines as hard as they'll go."
"I'm almost clear of the debris field - I should make it -"
"Something hits the bottom of the ship with a loud CLUNK."
"I hear a groan, then a crack."
"The next jolt knocks me unconscious."

scene bg black
with Dissolve(0.5)

pause(3.0)

"The shuttle rattles all around me."
"I can hear the alarm, but it's faint..."
"so faint."
"And then it's gone."
"Good. I can rest a little longer."
"It's warm..."
"and wet."
"I'm floating in the water."
"It feels good..."
"I reach out to taste some of it."
"Pain shoots up my shoulder."
"The feeling wakes me up."
"Where am I...?"

scene bg calypso-day
with Dissolve(3.0)

"I must be on the planet."
"Sitting up feels too difficult right now, so I turn my head."
"It looks like I'm in an ocean of some sort. It goes on as far as I can see in either direction."
"The air is humid and warm - just like the water - but there's barely any wind, and no waves."
"It's a good thing I didn't drink the water, I realize. Risk of bacteria outside, it must be extremely salty for me to float in it like this..."
"But I'm not exactly floating."
"I push one hand down into the water and it pushes back up on me."
"It's some sort of membrane."
"I press my hand outwards. The membrane goes on as long as I can reach."
"It feels organic..."
u "Are you awake?"
"I bolt upright."
"Pain takes me again, but I push it back this time to look around."
"I sink into the membrane."
t "Who - where -"
"I scramble to my feet, which sink deeper in. Stumbling, I run until I hit the edge of it."
"I fall into the water. I try to swim, but I can't move my arm all the way, and my legs are giving out."
"I gasp helplessly for air, but I start to sink."
"Then I feel the membrane under my feet again, and it pushes me back to the surface. I cough the water from my lungs."
u "I think you are awake."
"I wasn't just hearing it. I look all around. I can't get up again, so I huddle into a ball."
t "Who are you? Show yourself!"
"I lose my balance a little - not out of shock, but because the membrane has moved a little under me."
"It gathers in a spot in front of me and breaks above the surface. It forms a blob that becomes a silhouette - and then it has eyes."

show calypso shy

u "Hi."
"I can't quite tell, but it seems to be looking at me. Is this first contact?"
"I back away from it again."
"As I reach the edge of the membrane, I realize it's changed its shape under the water too."
"It curls upwards at the edges now so I don't tumble off into the water."
t "How can you speak my language?"

show calypso neutral

"The creature coagulates into a more humanlike form, though it can only replicate the top half - the other half melts into the water."
"Out of the strange membranous mass comes a single long appendage, which points off into the distance."
u "From your thing."
"I follow it with my eyes - it's right. My ship is floating a little ways away. It is damaged. The fact that it didn't break into pieces is impressive."
"Which reminds me..."
t "What happened to me? How did I get here?"
u "You fell from the sky."
t "And then?"
u "I took you out of your thing."
t "How long have I been unconscious?"

show calypso curious

"It gestures to my toe and then to my head with another appendage. When it is finishes its gesture, the appendage reabsorbs into its body."
u "You are that long."
t "No... I mean, how much time has passed since I arrived?"

show calypso thoughtful

u "...time."

"It doesn't seem to understand."
"I point to the sky."
t "How many times has the sun risen since I got here?"

show calypso curious

"It looks up again."

u "The sun rises?"
"Oh dear."
t "Are you a child? Do you have parents?"
t "Can I talk to your parents?"
u "Okay."
"The strange mix of pink, orange and blue that makes up the creature's body seems to roil around a bit. I'm unsure what that means."
"I wait for it to call its parents, and it stares at me."
"We remain like this for a while before I realize it's not planning on going anywhere."
t "Your parents? Can you get your parents for me?"
show calypso neutral
u "Yes."
t "Okay, where are they?"
u "They are here."
"More watery limbs form from the membrane. They gesture to the sea. They point down a little - perhaps its parents are under the water?"
t "But what about talking to them? Can I talk to them?"
u "You are talking to them."
t "But I'm talking to you."
u "Yes."
"I look down at the water again, then up at this creature."
t "Are you a representative of your species?"
u "A representative?"
t "A representative... an individual who speaks on behalf of the others."
u "Individual..."
"It sounds the word out, gesticulating with its limbs with each syllable."
u "I am an individual."
u "Are you an individual?"
t "...Yes. I am."
u "Can I speak to your parents?"
t "Uh... no. I'm an individual. My parents aren't here."
u "But you're an individual. Where is the rest of you?"
"I look down at my body, then at the creature's body. I think I can see other masses distantly in the water."
t "This is everything."
show calypso curious
u "Really? ... that's everything?"
u "Where are your parents?"
t "My parents are dead."
t "Along with most of my people."
show calypso sad
u "Dead?"
t "Do you not have death here? Do your people not die?"
u "I did. I remember it."
u "I used to die."
u "Do you still die?"
t "Eventually, yes. We all do."
t "That's why I have to get back to them."
show calypso shy
u "Is that what happened to the other things?"
t "Other things?"
t "I don't know what you..."
hide calypso
"It disappears back into the water. A moment later, we start to move."
"At first it looks like we're moving towards my ship, but when the ship doesn't get any closer even after a couple of minutes, I realize that the ship is moving too."
"In the absence of the creature - its humanoid form, at least - I remember the pain I'm in. I lie back down and feel the water lapping across my body."
"I haven't soaked in water like this in years."
"It feels like the baths I used to have as a child."
"Penelope might like it here."
"I wonder if there's land nearby."
"I lift my head to scan the horizon again, and to my surprise I see what looks like an island in the distance."
"Slowly this time, careful not to move my injured arm, I sit back up."
"I see what looks like a mountain - trees of some kind - a beach..."
"But then they come into focus."
scene bg calypso-island
"The whole island is made of shipwrecks."
"My ship floats ahead of us until it reaches the shore of this other island. It stops just next to it, and then out of the water, more membranous tentacles emerge, at least ten or twenty of them."
"They gently push the ship until it washes up on the shore."
"Meanwhile, we come ot a stop just off the edge of the island."
"From here, I can see the shipwrecks more clearly."
"There are ships of all kinds here... most of them are in tatters, but a few are intact enough to almost be pilotable."
"The bulk of this island is made up of one large ship. In its day it must have housed a crew of hundreds."
"Nearby I can see smaller islands jutting out of the water."
"They're made of all kinds of metal, with designs that boggle the mind in their complexity."
"What is strange is how they're gathered together. Some are welded into one piece, while others are placed precariously on top of one another."
"Other creatures like this one are tending to them, making sure they stay balanced and in good form."
"One is removing rust from a derelict ship; another is trying to place a small, round beacon on top of another ship."
"The beacon keeps tumbling off. The creature seems a little frustrated."
t "Do you collect these?"
show calypso shy
u "They fall from the sky. They tell me things about places I haven't been."
u "I put them together so I can come back to them and learn more."
t "And the others of your kind... do they help you with this?"
u "What others?"
"I point to one of the creatures."
u "That's me."
"Confused, I point to another one farther away."
u "That's also me."
"The creatures all stop what they're doing."
u "It's just me here."
t "I... see."
"No wonder my earlier questions made no sense."
t "Are there any others on this planet? Any other individuals?"
u "Why would there be?"
u "It's just me here. I collect things. The things tell me things."
u "Now you tell me things."
"A collective consciousness that perceives itself as an individual..."
"It's incredible."
"I remember what it said earlier about the sun rising, and it occurs to me that this being must span the entire planet."
"The thought makes me shiver."
show calypso neutral
u "Are you cold?"
t "No, it's nothing, I..."
"My eyes fix on one ship in particular."
"My heart skips a beat."
"I point at it with my bad arm by mistake, but I barely notice the pain."
t "That one..."
show calypso curious
u "They come to take places."
u "They came here too. But they fell like the others."
u "You're the first one who fell differently."
t "Can you bring me closer to it?"
"We float through the water until we're right in front of it."
"The metal is starting to rust."
"I touch the hull with my hand. I'm so used to hearing it humming, to smelling the smoke..."
"But it's gone here. It's dead."
u "Are you alright?"
t "You said they come to take places?"
t "They took my home."
show calypso sad
u "I'm sorry."
t "We barely escaped on a ship."
t "I was sent here to see if this could be our home."
t "I have to get back to them. They're waiting for me up there."
u "Back to the sky?"
t "Yes."
show calypso thoughtful
u "Your thing is broken."
u "It can't fly anymore."
"No."
t "Take me back to it. Take me to the shore."
hide calypso
"We drift back to the large island. When we approach the shore, I roll into the water and manage to swim the rest of the way."
"My ribcage throbs along with my arms, and my legs are aching. I wouldn't be well enough to fly even if I could."
"I clamber onto the metal of some old abandoned ship. It's steadier than I'd imagined."
"The ache in my legs makes my steps slow and deliberate, but I make it to my ship."
"My heart sinks when I reach it."
"The computer - and miraculously, the glass hatch - is intact, but everything else - communications, stasis, propulsion - is destroyed."
"I slump to the floor."
"There's no way I'll make it off this planet in this ship."
"A lump forms in my throat."
u "I'm sorry you can't bring your thing with you."
"I'm hurting too much now to get up again, so I roll over onto my back to face the creature."
show calypso curious
t "What is that supposed to mean?"
u "You want to go back to the sky, right?"
u "This thing won't go there. But I have some things that might."
t "You mean... other ships?"
u "Ships? Yes, yes, ships. I think so."
u "And something to make you sleep."
t "You would do that for me?"
show calypso happy
u "You're the first one to fall differently. The first one I remember, anyway. I have to return you."
"The metal is cold and grating, and somehow the water feels more inviting right now than solid ground."
"I carefully lower myself back into it."
"I paddle just a few strokes before the creature raises me up to the surface."
u "You should rest now. You're still hurt."
u "I'll gather what we need."

scene bg black
with Dissolve(2.0)

pause(1.0)

scene bg calypso-night
with Dissolve(2.0)

"It takes some time just to recover from my injuries enough to work."
"At first I survive on what little food we could salvage from my ship, but as that runs out, the creature starts to bring me its own food:"
"Strange-smelling sludge from the ocean floor, something that resembles an eel cooked on engine fuel from a derelict ship, fungi that taste saccharine sweet."
"I worry about local bacteria, but the creature uses old alien devices to scan my body and feeds me little bits of things to test my reactions."
"Sometimes it pokes me with an appendage while I'm not looking. It's innoculating me, I realize. And it's working: my stomach roils and grumbles but accepts what it's given."
"The creature seems almost excited to have a friend. It fusses over me, changes my bandages too often, adjusts its appendages to look like rough estimations of human hands - though that bothers me more than the formless alternative."
"My father used to read me Greek myths. The Odyssey was my favorite. This creature reminds me of Calypso, so that's what I start calling it. I give the same name to the planet: it only makes sense that they should have the same name."
"I never read it to Penelope. She was too young at first, and by the time she was old enough we were out here, and it didn't feel right."
"I named her for it too."
"It all seems too on-the-nose now."
"I try not to think of her."
"All I let myself think is that I'll see her soon."
"Once I've recovered enough, Calypso starts to bring me pieces from its collection. Some of the stuff it brings is entirely useless: tools built for different hands, baubles it thought looked interesting, indecipherable maps."
"After a while, though, it learns, and it starts to bring things I can use. A working propulsion system. An old but functional stasis pod, one that - to my amazement - allows for far longer sleeps than Earth technology."
"When it brings a communicator that miraculously uses radio technology almost exactly like ours, I lunge for it so excitedly that Calypso fails to catch me and I fall into the water."
"We decide to use my old ship as the shell, and in a day Calypso hollows it out."
"Eventually we have all the parts neatly stacked on the island, and we get to work putting them together."
"Calypso is better than I am at most tasks, but my hands are useful for more precise work. We divide the labour neatly."
"Sometimes we chat - about the meanings of words, about our cultures, about what Calypso has learned from its collection of other aliens."
"Mostly, though, we're just quiet."
"It breaks the silence one night, while we're working on the radio communicator."
show calypso neutral
c "Tell me about your planet."
t "What do you want to know?"
c "Just tell me what you want to tell me."
"I think about it for a moment."
menu calypso1_menu:
   "What do I want to tell her?"
   "About my life on Earth.":
     $ calypso1 = True
     t "Most of it was oceans, but I lived far from them, inland. I grew up in the country, near some mountains."
     t "It was a lot colder than this most of the time."
     t "My mother died when I was young, and my father joined the military, so he was gone a lot. My grandparents raised me."
     t "My grandmother always had lots of flowers around. She had some rare ones - sometimes she got quite a bit of money for them."
     t "When I had my daughter, I wanted to make a flower garden like that for her..."
     t "We couldn't, unfortunately. I wish she'd met my grandma."
     t "She takes after her, though. Still wants to make a new flower garden wherever we end up."
   "About the end of Earth.":
     $ calypso1 = False
     t "I'd guess that most of my planet is desolate by now."
     t "When the invasion started we'd destroyed large parts of it already."
     t "They didn't have to do much to take out our supply lines with the food shortages we had before they arrived."
     t "Fertility rates were down, too. Some people on the ark think we'll do better there than we would have on Earth."
     t "They said it was a miracle I had my daughter after being behind enemy lines for so long, and with the radiation in the area..."

label after_menu2:
show calypso thoughtful
c "Why did you have a daughter?"
t "Why?"
if calypso1:
   t "I wanted to bring something good into the world."
   t "I wanted to make it better, even if only a little."
   t "And I like to think that I did. That she did."
   t "I wouldn't wish what happened to Earth on anyone..."
   t "But I'd endure it a thousand times for her."
   jump post_calypso1
else:
   t "I saw so much being taken from the world."
   t "I wanted to bring something into it."
   t "I never thought about how she would feel, being born into all this..."
   t "Sometimes I feel guilty about it."
label post_calypso1:
c "But why do you have children? I mean... why do your people have children?"
t "We die, unlike you. Children are our only way of passing ourselves on."
show calypso neutral
c "I told you I used to die."
c "What I meant was, I used to be we. I used to be like you."
c "We had conflicts and families. Parents and children. Everything you've told me about."
c "I remember it sometimes, like a dream."
t "What happened?"
show calypso sad
c "We chose to become one."
c "At first it was only a few of us. But more and more of us joined. The others died. The ones who joined became me."
c "I am my parents. I am my children."
c "I've lived for so long that I don't know how to feel about it."
c "I don't remember what having children is like."
t "That's to be expected, isn't it?"
t "As your individual bodies die and new ones are born, you change."
c "I suppose. But I..."
c "I forgot what time was like."
c "And now there's you."
c "You made me remember."
c "I remember time and I feel like I've died. Like I've lost..."
"FZZZZZZZZZ"
"I bolt upright."
t "The radio!"
hide calypso
"I dive off of Calypso into the water and swim to the island."
"The communicator is perched next to the ship."
"I'm still not sure how to operate it, but it's glowing faintly."
"FZZZZZZZZZZ"
"It flickers with the sound. I adjust the frequency."
"FZZZZZSSS IS THE LAST CALL. WE REPEAT, THIS IS THE LAST CALL."
"I recognize that voice."
"It's that solder on the bridge. I picture his face: his wide and round cheeks, his freckled face. He always looks so nervous around me."
"It's the ark."
"THIS IS THE LAST CALL FOR SCOUTS SENT THROUGH THE G848 ASTEROID CLUSTER."
"IF YOU READ THIS MESSAGE, PLEASE RESPOND. WE WILL SEND ASSISTANCE. PLEASE RESPOND."
"I fumble with the device. A section pulls apart from the contraption."
"This must be the receiver."
"I hold it right up to my lips."
t "Ark, I read you! I'm on the planet! Repeat, I made it to the planet!"
t "It's habitable! Populated by a friendly life form! I'm repairing my ship, but I'll be on my way soon!"
t "Ark, please respond!"

pause(1.0)

"THIS IS THE LAST CALL FOR SCOUTS SENT THROUGH THE g848 ASTEROID CLUSTER."
"IF YOU READ THIS MESSAGE, PLEASE RESPOND. WE WILL SEND ASSISTANCE. PLEASE RESPOND."
t "Yes! I read you! Please respond. Please. I'm here."
t "I can make it back to you. I can meet you on another planet. Please give me your location."

pause(1.0)
"WE REPEAT, THIS IS THE LAST CALL."
"WE MUST CONTINUE ON OUR JOURNEY."
t "No, please!"
"I fumble with the radio, adjust the frequency, hit it as hard as I can."
t "Please respond!"
t "Please!"
"The radio goes silent for a full minute."
"Then, quieter:"
"This buoy is to commemorate those scouts killed in action at the G848 Asteroid Cluster."
"We are forever grateful for their service and their diligence in searching for a new home for our people."
"Though we cannot find their remains, we hope their spirits will come to rest with us wherever we land."
pause(1.0)
"This buoy is to commemorate those scouts killed in action at the G848 Asteroid Cluster."
"The message repeats over and over again."
"I listen to it."
"I wait for it to change."
"It doesn't change."
show calypso shy
c "But you're not dead."
t "They think I am. They gave up on me."
t "They're gone."
c "Can you follow them?"
t "I can, but when will I get to them?"
t "How long will it be?"
t "How will I even know where they are?"
t "They could die of old age before I find them."
t "Penelope..."
"I hold my head in my hands."
"Something touches my shoulder, tentatively."
"It's one of Calypso's limbs. It's warm and soft, and a little sticky."
"It feels surprisingly human."
c "I'm sorry."
c "I know how you feel."

scene bg black
with Dissolve(2.0)

scene bg calypso-day
with Dissolve(2.0)

"I find it hard to motivate myself after the ship leaves."
"But Calypso busies itself around me with improvements to the shuttle."
"Quietly, it leaves my tasks unfinished, and when there's no more work it can do on one part without my help, it moves on to another part."
"One day, I find myself working too."
"Bit by bit, we finish the ship."
"At first I count the days, but it occurs to me I have no idea how long the days are here."
"I don't know how long it's been since I last saw her."
"The thought makes me dizzy."
show calypso neutral
c "I found something you might like."
t "What's that?"
"A few of its limbs reach out to an islet nearby. They rifle through what looks like a bucket full of small items, each limb neatly holding one or two of the items while the others continue to dig."
"Finally one limb finds what they're all looking for. It holds the object up victoriously, then brings it to me and drops it in my hands."
"It fits neatly in my palm."
c "I taught it to speak like you."
c "It said it knows hundreds of languages."
c "It'll speak them for you."
t "How does it work?"
show calypso curious
c "You put it into your ear, I think... and then... it works."
"That's all it seems to know. Which is promising, but also kind of terrifying."
c "I found something else, but I already put it in."
c "It'll keep you healthy when you go to other places."
c "I told it about your body and what you need. It should be able to help."
"This must be how it innoculated me before."
t "Thank you."
show calypso shy
c "And... one more thing."
"This, it doesn't have to take from one of its islands."
"Instead, it seems to come from underwater - I feel a faint bubbling from under us, and then a limb emerges with a small, blue stone."
"It presses it into my hand."
"It hums faintly, and when I touch it with my fingertips it glows faintly pink."
"It looks like Calypso."
t "What is it?"
c "It'll let you through the sky. So you won't fall back down."
t "How...?"
c "Before... before I was me, we went to space too. We came back. We made it so that no one could follow us."
show calypso sad
c "I'm sorry we made you fall."
t "You couldn't have known..."
c "I didn't."
c "I had no idea that it would feel like this."
c "You gave me that."
pause(2.0)
c "You don't have to leave."
t "What do you mean?"
c "You have children to pass yourselves on, because you die. But if you don't die, then..."
c "I don't want you to die."
"Calypso reaches out and touches my hands. It presses them together, with the stone in the middle."
c "You can live here with me."
show calypso neutral
c "When you're ready, you can join me."
"It takes a moment for the gravity of what Calypso is saying to sink in."
"A life without death..."
"With no more pain, or cold."
"Everything I've known is dead."
"Is there anything left for me out there?"
if calypso1:
   "It would mean leaving my hopes behind. For Penelope, for our new home..."
   if truth:
      "But at this rate, Penelope might grow old without me."
      "What place do I have in her life, a mother who abandoned her?"
      "Would she be better off without me?"
   else:
      "Penelope could up without me, alone and scared and wondering what happened to me..."
      "My stomach turns at the thought of it."
      "What kind of a mother would I be to leave her all alone?"
      "What kind of a mother am I?"
else:
   "I'd be giving up on the ark... but on the mistakes, too. All the terrible things that have happened to me..."
   "I could leave them behind."
   if truth:
      "And Penelope. I'd be leaving her, too."
      "But what place do I have in her life now, anyways? A mother who brought her into this, only to abandon her?"
      "Would she be better off without me?"
   else:
      "But Penelope... what would she do without me?"
      "What is she going to do without me?"
      "I brought her into this, and now to leave her all alone... I could never forgive myself."
      "Even if I see her again, I might never forgive myself."
      "What kind of a mother am I?"

menu calypso2_menu:
    "I never thought I'd be thinking about this. But I want..."
    "to leave.":
       t "I'm sorry."
       if calypso1:
          t "I've been hoping for a better future my whole life."
          t "I can't let go of it."
       else:
          t "I know I've made mistakes."
          t "But I have to believe I can correct them."
       show calypso sad
       c "I understand."
       c "You can still come back."
       c "You can always come back."
       c "I'll be here. I'll wait."
       jump calypso_end
    "to stay.":
       t "I..."
       if calypso1:
          t "I've been hoping for a better future my whole life."
          t "But I don't want to spend my whole life waiting for something that will never come."
          if truth:
              t "Penelope will be so sad without me... but she'll move on."
              t "She'll grow up, and she'll forget me."
              t "Maybe it's better that way."
          else:
              t "Penelope will be so alone without me..."
              t "But I've already left. She's already alone."
              t "Whether I die looking for her or stay here, she'll still be alone."
              "I'm so sorry, Penelope... I hope you'll be okay without me."
       else:
          t "I've done so many awful things."
          t "And I'm so tired."
          if truth:
              t "Even if I do make it back, I'm not what my people need."
              t "Penelope is."
              t "She'll be sad without me... but she'll move on."
              t "She'll grow up, and she'll forget me."
              t "I think it's better that way."
          else:
              t "Penelope will be so alone without me..."
              t "But even if she's alone, it's better than being raised by me."
              t "And I've already abandoned her. I've already left. She's already alone, no matter what I do."
              "I'm sorry, Penelope... I hope you're be okay without me."
       show calypso happy
       c "Are you sure?"
       c "You can always change your mind."
       t "I know... but I won't."
       t "I think I was meant to land here."
       t "To leave my people behind... and to meet you, Calypso."
       t "To stay with you. To join you, someday."
       t "I'm just sorry I couldn't say goodbye."
       show calypso curious
       c "Maybe you will, someday."
       c "Maybe they'll find you."
       c "If they ever come back, I'll be waiting for them."
       c "No - we'll be waiting for them."


       scene bg calypso-night
       with Dissolve(2.0)
       "We don't join together immediately."
       "Calypso continues to collect ships, and I continue to help it."
       "It shows me its collections. It shares with me countless histories of peoples long dead."
       "For some, it knows what happened, while for others, all it has are fragments."
       "To think that humanity spent so long worrying we were the only life in the universe..."
       "And now I'm here, merging consciousnesses with this being I once thought of as so different."
       "I imagine that the joining will happen all at once, but it occurs in fragments."
       "Sometimes I wonder if it will happen at all."
       "But then I dream that I'm a planet, that my breaths are waves and that the days pass like shivers."
       "Another time I dream about a distant past, but I can't be sure if that past is the destruction of my planet or of some other place I can almost remember."
       "When I wake up from those dreams, it hurts less. Not because the pain is gone, but because it has dissipated over the ocean, over billions of bodies that shoulder it for me."
       "Finally, I dream of Calypso. I dream of moving in synchrony, of thinking thoughts together. I dream that my body becomes liquid and spills over it into the water."
       "I dream that I am alone, but that I am not alone, that I will never be alone. I dream that we are one and that we are everyone."
       "It is an intimacy I have never known."
       "I never forget Penelope. I don't think she ever forgets me..."
       "But one night, I dream of a future when a ship falls from the sky, and when I open the stasis pod, the face inside carries traces of her, traces that echo across years or generations or millenia."
       "I can't be sure... now that I think of it, I don't really remember what time feels like."
jump end

label calypso_end:

"This time I reach out. I touch its shoulder."
"My hand is shaking a little. The shivers turn into ripples across its body."
t "I will never forget you."
c "Never?"
t "When I find my people, I'll tell them about you. I'll tell Penelope, and she'll tell her children, and we'll pass it on down."
t "And I promise I'll find them."
t "So yes. Never."
c "Me too."
c "I will never forget you either."

scene bg calypso-night
with Dissolve(2.0)

"We finish constructing the ship together."
"Calypso is still sad that I have to leave. If I'm being honest, I'm a little sad too."
"But we enjoy what little time remains."
"On my last night, we use the energy core from a ship to make a fire on the island, and I show it how to roast foods over an open flame."
"It seems to notice the dark for the first time: the stars reflecting on the water, the smell of smoke, the precarity and excitement of not being able to see everything so clearly."
"I can tell it's in pain. I don't mean to hurt it."
"But there's nothing I can do about the passage of time."

scene bg calypso-day
with Dissolve(2.0)

"I climb into my ship."
"It looks the same from the outside, but inside it's completely redone, a confused mish-mash of different alien technologies."
"The screens come online."
"My location comes up on the map, the same flashing yellow dot as before."
"The ark's location is unknown."
"The ship seems confused as to how to communicate with its new components - it shows my stasis pod at 1577 percent power and my energy core as offline, even as the core buzzes to life and powers the screens."
"But it seems like everything's working."
"I poke my head back up out of the ship."
show calypso shy
c "Is everything okay?"
t "Yes. It's working perfectly. Thank you."
c "It was..."
show calypso sad
c "It was my pleasure."
"I try to smile at her, but all I can do is nod."
"I close the hatch."
"I turn the propulsion on, and slowly, carefully, I push my fingers down on the control panel."
"The ship lurches forward. At first it looks like it's going to fall into the water -"
"But at the last moment it pulls upwards and tilts its nose towards the sky."
"As it makes the ascension, I look back down at Calypso. Its humanoid form is gone, but from up high, I can see under the waves so many silhouettes."
"There must be millions of them."
"I watch them until they disappear beneath the haze that blankets the planet."
t "Goodbye, Calypso."
if calypso1:
    t "And thank you."
else:
    t "I'm sorry."

scene bg space
with Dissolve(2.0)

label space1:

"I'd wondered if Calypso's stone was meant as a metaphor, but when I emerge into space, the debris clears a path for me."
"I make it safely out of the field."
"And now I'm alone again."
"I slow the ship and check the map."
"The commander mentioned five planets. One of them was Calypso, of course... but three others are nearby. The ark could have gone to any of them."
"Calypso was kind enough as to give me what information it had on them, but it was very little."
"There's a larger planet, almost the same distance from its sun as Earth was from ours. Its sun is a little smaller, so it should be just a little cooler. On the map, it looks like a green dot."
"There's a smaller planet closer to its sun. Calypso said that it's supposed to be warm and dry. It's an orange dot on the map."
"The last planet rotates on a strange axis. It should have more extreme temperature variations that I'm used to. It's a blue dot on the map."
"It's unclear which one the ark would be most likely to go to, and the commander had even less information that I do."

menu:
   "The decision seems arbitrary, but I have to make it now. Where do I go first?"
   "The green dot.":
     $ green1 = True
     $ orange1 = False
     $ blue1 = False
     jump green1
   "The orange dot.":
     $ orange1 = True
     $ blue1 = False
     $ green1 = False
     jump orange1
   "The blue dot.":
     $ blue1 = True
     $ orange1 = False
     $ green1 = False
     jump blue1
label after_menu4:

label green1:

"I type in the coordinates for the green planet."
"It looks like it would harbor the most similar climate to Earth, given the distance to its sun..."
"I'll take that small hope. It's better than nothing."
"The ship lurches forward, and then the stars are a blur all around me."
"I watch them go by for a while. I look at the screens one by one. I examine the control panels, trace out the alien lettering on my chair, and poke at the innoculation machine."
"I do anything to avoid stasis for just a few more minutes."
"But then my mind wanders to Penelope."
"What is she thinking right now? Does she miss me?"
"What does she think about when she thinks about me?"
"My stomach ties itself in knots."
"I recline my chair and press my arms into the armrests."
"I let the needles prick me and imagine myself staring up at the sky from solid ground, on a planet with fresh air and clean water where I can make a home."
"Is that planet Earth? Is it Calypso? Or is it a place I'll never find?"
"The thought haunts me as I drift away."

scene bg black
with Dissolve(2.0)

p "Mom?"
p "Do you know who my father was?"
p "Can you tell me about him?"
if truth:
   if calypso1:
      t "Your father..."
      t "I don't know they'd want you to call them that."
      t "They told me to forget."
      t "I have to forget."
   else:
      t "Your father..."
      t "I don't know they'd want you to call them that."
      t "They told me to forget..."
      t "But I can't."
      t "I'm so sorry, Penelope. But I can't."

else:
   if calypso1:
      t "Your father..."
      t "Your father is dead."
      t "They told me to forget."
      t "I have to forget."
   else:
      t "Your father..."
      t "Your father is dead."
      t "They told me to forget..."
      t "But I can't."
      t "I'm so sorry, Penelope. But I can't."
p "Why do we have to forget?"
p "Why can't we remember things, mom?"
p "I forget the taste of coriander."
p "I forget what the flowers smelled like."
p "I forget what you looked like."
p "Why do I have to forget?"
p "Why did we never take a photo together?"
p "Mom..."
"I hold Penelope's face in my hands."
if truth:
   "To help her."
else:
   "To comfort her."
"But she has no face."
"She has no face because I have forgotten her face."
"I have forgotten her and she has forgotten me, and she slips from my hands and becomes the waters of Calypso, and they pour over me and fill my ship until everything is dark."

scene bg space
with Dissolve(2.0)

"I wake up a little at a time, and then all at once. I gasp sharply and open my eyes with a start."
"I feel as if I've almost drowned, but my body isn't starved for air."
"Suddenly full of a jittery, fearful energy, I pull my chair forward."
"The planet is dead ahead."
"When I first look at it, I have to convince myself that I haven't returned to Earth."
"Its continents are larger, yes, and they're different shapes - but the bright greens and calm blues, cut across by languid clouds..."
"It's like home."
"As we pull in, there is one distinct difference:"
"This planet has scars."
"Some of them are from mining, but from the looks of it, vast tracts of this land were once covered in cities and factories."
"But the cities are dark."
"Even from up here it's clear they've been long abandoned."
"I turn back to my screens. They're reading no beacons or signals from the ark..."
"But I'm low on food, and my energy core's readings are fluctuating dangerously."
"It needs a rest. So I have to land."
"I pick a spot that looks as clear as possible of the cities and structures that litter the planet's surface."
"The ship makes a smooth landing just near what looks like a forest."

scene bg field-day
with Dissolve(2.0)

"When I open the hatch, I find myself at the edge of a vast field."
"Hills roll on as far as I can see."
"The sky is dotted with tiny puffy clouds."
"In the distance, I can just barely see the tips of buildings."
"They must have been magnificent once. But even from here I can see that they're dilapidated."
"On a hill far away, there's a herd of some sort of animal - I can't really see them from here, but it looks like they're grazing. But besides them, I'm alone."
"I gather my gear, step out and close the hatch behind me."
"I sit down in the grass and lean back on my hands."
"It's softer than on Earth. It feels like a pillow."
"The air is clear and smells faintly sweet."
"This is pleasant... and pleasant is something I haven't felt in a while."
"I should look for some food. If that innoculation machine did its job right, it should be safe. And I'll need to eat something before I go back into stasis."
"But for now, I decide to just take in the moment."

pause(1.0)

"I'm cloudwatching, almost tempted to take a nap, when I hear a faint rumbling."
"I scan the fields. They look empty and just as beautiful as before... except for..."
"The animals from before."
"They're heading straight for me."
"I leap to my feet."
"Is this a stampede?"
"Where can I hide?"
"Should I get back in the ship?"
"But its engine is recharging - it'll take too long to--"
"HSSSSSSSSSSSSS"
"There's someone behind me."
"I turn around slowly."
show scout angry
"This clearly isn't just a herding animal - it's wearing clothes."
"How did I not see that from so far?"
"The rest of its kind are far behind, running up a distant hill. This one must be faster than the others."
"It studies me for a moment, then hisses again. This time I hear the complexity of the sound - it sounds like a language."
"Keeping eye contact, I reach my hand up and flick my universal translator on in my ear."
u "... you come from? Who are you?"
t "I'm... I came from the sky. I'm a human. I was on a ship with others like me, but I lost them. I'm searching for them."
u "Are you a builder?"
t "What?"
u "Did you build this?"
"It makes a gesture towards the buildings."
t "No. We're from far away... we've never been this far from home."
show scout curious
"It turns towards the rest of the flock, then looks back at me."
u "And your kind left you alone?"
t "Yes."
u "I am so sorry."
"The creature's candor is surprising."
t "Thank you."
show scout suspicious
u "...This is your ship?"
t "Yes. It's my shuttle. To get back -"
u "They will claim it."
"I take a step back."
"My hand reaches for my weapon."
t "This is my ship. I won't let them take it."
u "But they will, and they'll kill you."
t "They'll try."
"I draw my gun."
u "Listen to me."
u "We have enough fighting right now. We don't need skirmishes with well-armed outsiders."
u "But if you look like you're fighting with me when they arrive, they'll kill you."
u "We are three thousand strong. Your weapon will be ineffective."
u "Surrender to me. You'll live, and I'll make a case for you keeping your ship."
u "Or pull that trigger and see how far it gets you."
t "...Why offer to help me?"
show scout happy
u "A short, squishy alien shows up on a hunt. I could kill it, but the trophy is far better looking alive."
u "And friendlier with me."
"That sentence should unnerve me, but the stampede of aliens - who, now that they're closer, I can see are very heavily armed - unnerves me more."
"I holster my weapon."
t "Okay, okay."
show scout suspicious
u "Okay. Now get on the ground."
"I get on my knees and put my hands in the air in surrender."
"My captor gives me a confused look and swats at me."
"When I don't move my arms, they take one in their own and pushes it downwards."
u "Why are you being hostile? Just put them on your knees."
"I do as it says."
t "Do you have a name?"
u "A what?"
t "What should I call you?"
s "Ah. I'm a scout."
t "No... I mean you. Like, I'm..."
s "You're a traveller. And I'm a scout."
s "Now we know each other."
"I can't tell whether they're being facetious or honest, but I don't have time to debate them -"
"The rest of the flock arrives."
"My captor takes a spear from a holster on their back and points it at my neck."
"The first to reach us look completely different from the scout - they have broader faces and longer fringes on the tops of their heads. Their shoulders and legs are broader."
"All of them are built for running, but these ones look like they're made to fight."
"They surround me in a wide circle that encompasses the shuttle as well. Some of them jostle the scout, but the scout stands their ground."
"Next come a group with long arms, narrow shoulders, and all kinds of heavy items hitched to their backs. On closer inspection, I see that what I thought were some trace of wings are actually rudimentary hands."
"Behind them I can see other shapes and sizes of the species - ones with wide hips carrying food, short ones holding young or tending to what looks like some sort of pack animal."
"I glance back at my scout. Compared to the others, they're taller and leaner. They certainly look faster - even their face looks more aerodynamic."
"Their eyes dart back and forth. When I see them linger on one especially large and stocky individual, I realize they're assessing threats."
"What did this scout get me into?"
"The circle parts at one end, and what looks like their leader emerges."
"This one is larger and taller even than the scout, but with long arms like the book-carriers."
l "Happy hunting!"
"The flock repeats the phrase. I find myself flinching."
l "It looks like our scout has found us something very special."
"I look up at the scout, and dearly hope I haven't misplaced my faith."
show scout neutral
s "That's {i}someone,{/i} leader."
s "This traveller has been separated from their flock."
s "They landed on our planet looking for their kind."
"The leader looks me in the eye for the first time."
l "I'm so very sorry."
"A few of the flock repeat his words."
t "Thank you."
"Murmurs erupt among the flock."
l "They have technology!"
l "A translator at the very least! And we haven't even gotten into their ship."
show scout angry
s "No... we haven't. The traveller has agreed to give us the schematics for all of their technology. The knowledge of their people."
s "We could have one energy core... but imagine what we could do with the knowledge of how to build more!"
"I resolve to speak to the scout about making unfair deals without my consent later."
"Meanwhile, the leader looks unconvinced."
"They turn to me."
l "And you say you can build an energy core like the one in your ship?"
l "How many can you make for us?"
t "I... I'm not sure I can..."
s "Please, leader. She isn't a tinkerer. She's a traveller."
s "But working with {i}our{/i} tinkerers..."
"The leader pauses to think. The whole flock falls silent."
l "Take the ship apart to carry. Kill the traveller and take whatever tech they have in their body."
l "Happy hunting, scout."
"The front lines of the flock step towards me. I jump to my feet and reach for my gun, but before I can draw it the scout steps in front of me."
s "This is my find, leader. I have a right to decide how it's dismantled."
"This gives the leader pause. He glances at me once more, then sighs."
l "I suppose you're right about that."
l "Fine. You can decide who gets what, including your traveller."
l "Since this is such a large prize, we'll camp here for four nights."
l "But we can't afford to stay any longer. After that, we take apart the ship and give what remains to whoever can tinker it."
l "That goes for your traveller, as well."
"The flock stays in formation around us a little longer. They seem surprised by what has transpired."
l "To your posts!"
"Finally, they disperse, moving into what looks like a pre-arranged formation of small groups."
"One by one, they unhook cloth from packs on their backs, tying and pulling them until they form interwoven rows of tents."
"I realize I've been holding my breath, and let it out all at once. My hands are shaking a little."
"I'm surprised when a fair few of the flock approach me to offer their condolences..."
"But it doesn't seem to garner me anything more than sympathy."
s "I thought I could get you more..."
s "I'm sorry."
t "I've heard enough half-assed apologies for today, to be honest."
show scout sad
s "They're not apologizing for your bad luck."
s "They're apologizing for your life."
s "For us, when you're separated from your flock, for all intents and purposes you're already dead."
s "It amazes me you still want to live on."
"My legs are shaking a little too - but from hunger, anger or shock, I'm not sure. I prop myself up against my ship."
t "I have to get back to them."
t "I have a daughter."
if truth:
   t "She misses me."
else:
   t "She needs me."
show scout curious
s "You have a daughter, and you're a traveller?"
s "Were they out of warriors or something?"
"Great. On top of everything else, these aliens are sexist?"
"I sigh again and sink to the floor."
s "You need some food."
"I look up at them. If they think I'm moving from my shuttle after all of this, or doing anything they say, they're insane."
s "I promise they won't touch it."
s "It was my find, and the leader agrees."
s "Now, I can bring your food here, but half of the flock is going to be staring at you if you stay."
s "If you'd rather be alone for a few moments, you can use my tent."
"They extend a hand to help me up."
"I want to stay here... but they're right. If I'm going to find a way out of this, I need time alone first."
"I take their hand and I get back up."
"They lead me down a makeshift lane."
"In just a few minutes, the field has transformed into a city."
"The smaller, interconnected tents I saw before are residential; now the larger tents are coming up too."
"I see what looks like an infirmary, a dining tent, and a tent especially for children."
"The scout stops by the dining tent. I wait outside, and they emerge with two bowls of food."
"They're reminiscent of rice bowls: meat roasted in a tangy sauce on some sort of grain, topped with what looks like grass but smells a little bit like garlic."
"I take one and try to stop my stomach from rumbling - though come to think of it, they probably wouldn't understand the meaning."
"We walk up the hill after that and find ourselves at the edge of the forest."
"The scout sets their tent up here, far from the others."
"It takes only a few minutes, and when it's done, it's larger than I expected, with enough room for us to sit comfortably away from the two makeshift beds they've set up."
t "Is it considered rude to pitch your tent away from the others?"
show scout happy
s "Not if I have a find I want to defend."
"I'm not sure what I think about being their find, but I'm too hungry to care at this point. I dig into the food."
t "This is delicious."
t "I don't think I've had home-cooked food in years."
s "What do you mean, home-cooked?"
"I eat a little too quickly, and my stomach starts to turn."
"I push the bowl away in front of me."
t "Back home, you could eat out, at restaurants. Or you could eat with your family at home. If you had a good cook in the family, home-cooked meals were considered a treat."
if calypso1:
   t "My grandmother's food was the best. She made this incredible pot roast..."
else:
   t "They tried to have cooking nights in the military, but they were always terrible. It's been so long since I've had someone cook something nice for me."
show scout neutral
s "So how large were your families? And how many of you became cooks?"
t "Oh, no. I mean... I've always been bad at cooking, but my grandmother was great at it."
s "So she was the cook, and you were the traveller? And you were a warrior... but you were also a mother?"
s "And she was, too?"
s "How many people {i}were{/i} you?"
t "Just... one?"
t "I do lots of things, but none of them are who I am."
show scout angry
s "That makes... very little sense."
"My stomach rumbles again despite my attempts to stop it."
t "Just... let me finish my food, and I'll explain it again."
show scout neutral
"They seem to understand it better when I explain it a second time."
"They take the opportunity to explain their culture to me as well."
"They're nomadic, which doesn't surprise me."
"They wander these parts looking for useful technology from whatever left behind all of these cities."
"And they really do define themselves by their one job: tinkerers, warriors, scouts, child-rearers, gatherers and so on."
"Each individual is assigned a job based on their biology: the strongest individuals become warriors, while the fastest become the scouts."
"And contrary to what I thought before, they're not sexist - in fact, the scout doesn't seem to understand the concept of gender at all when I explain it to them."
"When I explain that different people were assigned roles and expectations on Earth by their sex organs, they seem totally incredulous."
"But the idea that shoulder width and arm length should determine someone's entire life path is only natural, of course."
"I get the impression the scout is lonely - they seem happier to talk to me than they are about the tech in my ear, which they've barely noticed since I arrived."
"Finally, when it sounds like we both have a rough handle on each other's culture, we fall into an awkward silence."
"Quite full now, I pick absent-mindedly at the last grains of food in my bowl."
s "I'm sorry for how you're being treated here."
s "I want to wait a few nights... if we broach the idea with the leader again in private, and if we explain to him what you explained to me, we might be able to change his decision."
s "We're just... we're a little on edge."
t "What is it?"
show scout sad
s "We're at war."
s "There are flocks who are tired of chasing tech. They've settled down near the old cities."
s "They don't care that we can't operate them. They just think it's safer."
s "The problem is, they've settled on land we're supposed to be chasing. They're pushing us out of our own territory."
t "So they're killing you for it?"
s "They weren't at first. Our leader has been mounting offenses against them, trying to push them back out."
s "I was hoping it wouldn't come to blows. But it's looking like it will."
s "We used to be a lot kinder to travellers."
t "You've had others?"
show scout curious
s "Of course. It didn't strike you as odd that no one was surprised that an alien landed in the middle of our field?"
t "I just thought you were excited to get to hunt something new."
s "Well, that too."
show scout angry
s "It used to be an exciting time for us. We'd share tech and food and stories. To think that things would get this bad..."
s "I'm sorry you had to show up now."
t "Why not join the flocks by the cities?"
s "Our leader would never go for it."
t "Then go without your leader."
t "You can scout for them."
s "Leave the flock? Scout for some other flock that doesn't even move?"
s "These are the kinds of things only a traveller could say."
t "Was I insensitive?"
show scout happy
s "It's refreshing."

scene bg black
with Dissolve(2.0)

"My bed is small and the blankets are thin, but the grass is so soft that I sleep as if in a luxury bed."

scene bg field-day
with Dissolve(2.0)

"I wake up early the next morning. I fold the blanket up and put it at my feet. The scout is still asleep."
"Quietly, I slip out of the tent."
"I walk along the hillside, keeping out of sight of the alleys and walkways in the makeshift town below."
"Finally I can see my shuttle. I lie down behind the hill and survey the area."
"It's a small ways away from the tents, but they're close enough that it would be hard to leave without hurting someone."
"I could manage it, but not without some sort of distraction."
"As the scout promised, though, it's untouched. For now."
s "Getting the lay of the land?"
"I look up."
show scout happy
"Their expression is something resembling a grin. Waiting for me to clue into something."
"Lay... land... I am laying down on the land."
"Was that a pun?"
"How does the translator even deal with puns?"
t "I'm just... making sure everything's alright."
s "Of course it is. For the next three days, at least."
s "But sneaking around isn't going to help your case."
"It doesn't escape my notice that they're speaking in hushed tones."
t "You made it very tempting, keeping your tent so far from the others. And up on this hill, too."
s "I have no idea what you're talking about. I just like the view."
hide scout
"We enjoy the view as we walk back to the tent. Soon after we return, the town comes to life as the others wake up."
"The day goes well. The scout leaves me alone for the most part, apparently to speak with important figures in the flock about my situation."
"They seem to think it's best if I stay away from those conversations, and I follow their lead."
"So I spend the day wandering the town, making small talk with those members of the flock who will talk to me, and watching the warriors' shifts."
"It occurs to me, as I eat dinner overlooking the town, that I'm feeling nostalgic."
"I've missed this."
menu:
   "I've missed..."
   "The simplicity.":
      $ simplicity = True
      $ danger = False
      "Life in the military was complicated."
      "Life on the ark was complicated."
      "It's been a long time since I've had a simple problem to solve..."
      "...and no one depending on me."
      "The implication of that thought hits me hard."
      "I feel guilty even thinking it to myself."
      "But I shouldn't."
      "I don't have room for guilt right now, I decide."
      "All I have to do is wait for the right moment and get out of here."
      "I can unpack my guilt later."
   "The danger.":
      $ danger = True
      $ simplicity = False
      "I miss being afraid for my life."
      "I wonder briefly what that says about my psyche."
      "But the truth is, I've always been drawn to the thrill of it."
      "The soldiers back on the ark think I volunteered out of a sense of duty -"
      "That it was an ambush that got me behind enemy lines."
      "The truth is, I wanted to be there."
      "I've missed not being there."
      "It feels good to admit."
label after_simplicity:

scene bg field-night
with Dissolve(2.0)

"Night falls, but the scout hasn't returned yet."
"I listen for activity downhill, but most of the town has turned in for the night... I wonder where they could be."
"It's even quieter around the shuttle."
"Quiet enough that I could sneak down - maybe even open the hatch - without anyone noticing."
if simplicity:
   jump no_escape
if danger:
   jump try_escape

label no_escape:
"I shake my head. It's too risky."
"If I tried to escape and got caught, it could ruin any hopes of a peaceful negotiation."
"And truth be told, I really don't want this to get violent."
"I lie down in my bed in the grass and stare up at the roof of the tent."
"I don't notice my eyes close."
"I'm starting to drift off when I hear the scout slip in."
"They pause at the doorway for a moment, then make a low growling noise. I hear the wall of the tent rustle - did they just punch it?"
"That doesn't bode well for me."
"They change into their nightclothes and lie down. They're still growling - it's low and barely audible, like an angry purr."
"I wait for them to get settled, then roll onto my side."
"They jolt a little at the sound."
s "Are you still awake?"
t "Yeah."
show scout sad
t "What happened?"
s "Arguments. Counter-arguments. Every day this war is more popular."
s "Is your flock like this?"
t "I'd be surprised if all flocks weren't like this."
s "I just can't change any of it. I can see where it's going, and I can see how terrible it's going to be, but I'm just a scout. Changing course isn't my job."
s "That's what they tell me, anyways."
"I laugh a little to myself."
show scout angry
s "What is it?"
t "It's just... earlier today I caught myself thinking how happy I was that I could watch someone else's problems instead of dealing with my own."
show scout curious
s "At least someone's getting something out of all this."
t "I understand, though."
t "I was where you are."
t "Seeing something terrible happen but being utterly unable to do anything about it."
show scout sad
s "How did you deal with it?"
t "I made myself necessary enough that they couldn't ignore me."
t "When people respect what you can do, they listen to you."
s "What, were you some kind of war hero or something?"
t "...Actually, yeah."
show scout curious
s "Oh."
t "My planet was invaded. I got trapped behind enemy lines..."
t "No one remembered me before that."
t "After I got back? I could have done anything and they would have listened."
s "Did it get better when they listened to you?"
if calypso1:
   t "It was still hard, but... yeah."
   t "It's easier to deal with these kinds of things if you feel like you can at least {i}try.{/i}"
   t "Even if it doesn't mean much in the end."
else:
   t "Not really. Whether or not you have any say in it, the same bullshit still goes on."
   t "It was more like... I was at peace with it."
   t "And I knew I had the power to at least make a little difference in people's lives."
   t "Even if it didn't mean much in the end."
t "Anyways, by the time I got back, there wasn't much hope for us."
t "I don't think there's anything I could have done."
s "What happened to your planet?"
t "It's gone."
show scout sad
s "I'm sorry."
t "And I'm sorry for your flock."
s "I just..."
s "Part of me just wants it to be over. No fighting, no war, just a clean end to it. You know?"
"I reach over across the grass and take their hand."
t "I know."
"They pull their hand away from my touch, and I wonder if I've done something wrong."
"But then they rest it on my shoulder instead, and slide closer to me."
"Our bodies are almost touching."
s "Sorry to unload all of this on you."
t "I'm a perfect stranger, right?"
t "Either I escape with your secrets or die with them in two nights."
s "Sorry for that, too."
t "Like I said, it's a nice problem to have to deal with. I'm not having trouble picking a side here."
t "I don't envy your position."
t "But you're not alone in it."
s "...Thanks."
"I lay awake for a while listening to what I think is their heartbeat."
"But its slow, unfamiliar rhythms and the warmth of their body lull me towards sleep."
"For just a moment, I remember the last time I was curled up next to someone like this."
"They told me not to remember them like this. I promised them..."
"But those were simpler times."

jump escapeatdawn

label try_escape:

"I slide my bag over my shoulder and slip out of the tent."
"Holding my breath and treading as lightly as possible, I make my way along the treeline where it's darker."
"Finally, I'm just up the hill from the shuttle."
"If I make a run for it, I can have the hatch closed before anyone sees - I'm certain of that."
"I take a couple of deep breaths, clench my hands into fists, and kick off to a sprint."
"I make it a couple of steps before someone tackles me to the ground."
"I prepare to fight for my life -"
show scout angry
"But it's the scout. I relax."
"They hold me to the ground, one hand on my chest. Still worried I'll try to get away, apparently."
s "Did you really think you'd be able to outrun me?"
t "You didn't even give me a head start."
show scout suspicious
"They make a sort of sputtering growl, something like a guttural tsk-tsk."
s "Let's get back to the tent before someone sees that embarrassment."
"They pull me up with them as they stand back up."
"They turn back towards the tent... but I don't follow them."
"I smile to myself and take a step back."
"They take a few steps before they realize I'm not behind them."
"When they catch me again, their movements are a little more desperate."
"Instead of tackling me to the ground - I'm too close to the hill and the shuttle for that - they pick me up."
show scout happy
s "You're liking this, aren't you?"
s "I could get in serious trouble for keeping your ridiculous escape attempts a secret, and you're having fun with it?"
s "Do you have a deathwish or something?"
"I smile at that."
"They're still holding me."
"We notice the touch at the same time."
"I escape their hold easily enough, but this time, instead of running for the shuttle, I run into the darkness of the forest..."
"And when they catch me, they push me to the ground and I pull them down after me."
"We chase each other a few times, hidden from the town by the hill and the darkness of the trees."
"When we finally get to the catching, our bodies fit together better than I'd imagined."
"We explore and feel each other, try each other out, experiment."
"It is a good hunt."
"Afterwards, we lie in the grass. It's even softer here in the woods than on the field."
t "When you said you've {i}had{/i} others like me before..."
s "None quite like you."
s "But I'd be lying if I said this was the first time I've been with a traveller."
s "And what about you?"
s "Yesterday you looked like you were ready to kill all of us to get to your shuttle."
t "I still am, of course."
t "I just remembered how much I enjoyed the thrill of it."
"I sit up on my elbow and kiss them again. They're still not used to it, but they're not entirely repulsed by it either."
show scout curious
s "You know... you're right."
s "When I walked back to the tent tonight, I was furious."
s "I spoke to the leader about your situation and he just won't listen."
s "He won't listen about the war, either."
s "I feel like I'm watching a catastrophe in slow motion, and I can't do anything about it."
s "But you're right."
s "There's something incredible about breaking the rules..."
s "...about being chased."
show scout happy
s "Maybe I'll become a spy."
t "A spy? For the other flocks?"
s "I don't know if they'd have me."
s "But it's better than watching this all go to hell and doing nothing."
s "Sorry to unload all of this on you."
t "I'm a perfect stranger, right?"
t "Either I escape with your secrets or die with them in two nights."
s "Sorry for that, too."
t "Like I said, it's kind of fun."
t "And I've found my way out of worse situations before."
"They pull me down on top of them, and for the first time try kissing me."
"The attempt makes me laugh, but they're a fast learner."
"At some point - though it's hard to pinpoint when - we make it back to the tent, and exhausted, I fall asleep next to them, thoroughly thrilled."

jump escapeatdawn

label escapeatdawn:

scene bg black
with Dissolve(2.0)

"I wake up to someone shaking me."
s "Come on! We have to go!"

scene bg field-night
with Dissolve(2.0)

show scout suspicious

t "What is it? What's going on?"
s "Your chance."
"The scout pulls me to my feet before I'm even awake enough to operate them."
"I come to my senses and grab my bag before they take my hand and lead me out of the tent."
"It's barely light out."
"Distantly, in the direction of the abandoned city, I can see the silhouette of another flock, lit by a few lights at their perimeters."
s "They're preparing for an attack."
s "Most of the others are asleep, and when they wake up they'll be more concerned about the army on the horizon than you."
s "We can get you to your shuttle and you can take off while they're still disoriented."
t "Will you be okay?"
s "I'll manage."
"We take off at a sprint across the hillside and down to the shuttle."
"It's a sprint for me, at least - for the scout it's a light jog."
"We hide between the shuttle and the hillside where it's still light."
show scout angry
s "Alright. You get in and get your engine going."
"The scout produces a couple of small spheres from a holster in their bag."
s "I'll distract them."
"The look on their face says that whatever those spheres are, they're dangerous."
t "You'll {i}what?{/i}"
t "If you get caught, you'll..."
if simplicity:
   s "I don't care."
   s "You're right. I miss things being simple..."
   s "And this is simple. I want to do this for you."
if danger:
   s "I'm a spy, remember?"
   s "I won't get caught."
   s "And it's so much better than doing nothing."
"I cup their face in my hands and kiss them."
if simplicity:
   "They look utterly confused by the gesture at first, but when I pull away and look into their eyes, I think they understand."
if danger:
   "When I pull away they kiss me once more."
"I press my hand onto the hatch and it opens. I climb up into the shuttle."
s "Don't forget me, Traveller."
"They take my hand."
"I can hear rustling in the tents nearby - the others are starting to wake up."
menu:
   "But I have to say one more thing."
   "I'll miss you.":
     $ missyou = True
     $ okbreak = False
     t "I'll miss you, Scout."
     t "If I can ever come back... I will."
     s "That's not your job."
     s "But thank you. Truly."
   "I won't forget you.":
     $ okbreak = True
     $ missyou = False
     t "Never."
     t "I'll never forget you, Scout."
     t "Good luck out there."
     s "Thank you. Really."
label after_okbreak:
"Scout squeezes my hand one more time and then lets go."
"They turn from me and disappear towards the tents."
hide scout
"I close the hatch, pump the accelerators to max and get the shuttle off the ground just as the others notice I'm in it."
"As I pull up, I hear a crack below me."
"I look down. A few of the tents are on fire."
"But Scout is long gone."
"They were too fast for the others."
"I give one last look to the field and then turn to the sky."
"The energy core comes to life and then I'm rising up through the atmosphere and back into space."

scene bg space
with Dissolve(2.0)

"I take a deep breath."
"Alone again."
if okbreak:
   "I'll never forget them."
   "I've made that promise before. I can make it again..."
   if calypso1:
     pass
   else:
     "Even if it hurts more every time I make it."
if missyou:
   "Part of me wants to turn the ship around and go back."
   "Scout was right... it's not my job."
   if calypso1:
      "If only it were."
   else:
      "But maybe someday it can be."

jump space2

label orange1:

"I punch in the coordinates for the orange planet."
"A warmer planet might be more promising for settlement..."
"It's a slim chance, but I'll have to take it."
"I engage the ship's engines and watch the stars turn to blurry lines out the window."
"Penelope always preferred the cold."
"She was a weird kid like that."
"I suppose she never got to do anything fun in the heat, so for her it was just uncomfortable."
"She never got to go to the beach on a hot summer's day, or take a nap in the warmth of the sun..."
"If she had, would she still prefer the cold?"
"Or is she sitting on that planet right now, feeling uncomfortable and grumpy that of all the planets in the galaxy, they had to pick the hot one?"
"I wouldn't have let them pick the hot one, I think as I recline the chair and slip my arms into the armrests."
"Even if we had to go it alone, I would have made sure we built our home somewhere she liked."
"The thought lingers with me as I drift into stasis."

scene bg black
with Dissolve(2.0)

p "Mom?"
p "Do you know who my father was?"
p "Can you tell me about him?"
if truth:
   if calypso1:
      t "Your father..."
      t "I don't know they'd want you to call them that."
      t "They told me to forget."
      t "I have to forget."
   else:
      t "Your father..."
      t "I don't know they'd want you to call them that."
      t "They told me to forget..."
      t "But I can't."
      t "I'm so sorry, Penelope. But I can't."

else:
   if calypso1:
      t "Your father..."
      t "Your father is dead."
      t "They told me to forget."
      t "I have to forget."
   else:
      t "Your father..."
      t "Your father is dead."
      t "They told me to forget..."
      t "But I can't."
      t "I'm so sorry, Penelope. But I can't."
p "Why do we have to forget?"
p "Why can't we remember things, mom?"
p "I forget the taste of coriander."
p "I forget what the flowers smelled like."
p "I forget what you looked like."
p "Why do I have to forget?"
p "Why did we never take a photo together?"
p "Mom..."
"I hold Penelope's face in my hands."
if truth:
   "To help her."
else:
   "To comfort her."
"But she has no face."
"She has no face because I have forgotten her face."
"I have forgotten her and she has forgotten me, and she slips from my hands and becomes the waters of Calypso, and they pour over me and fill my ship until everything is dark."

scene bg space
with Dissolve(2.0)

"I wake up to a red glow."
"Is it sunlight?"
"How long was I napping for? Is it sundown already?"
"I open my mouth to call to my grandma."
"Please tell me I didn't oversleep again..."
"But I didn't oversleep. The stasis pod always wakes me up ontime."
"No, the red glow is from the planet, hovering above me."
"It's almost entirely orange and red - deserts lined with oxidized iron, from the looks of it."
"Lines of green and blue slice and swirl across it. So it must have some fresh water. I wouldn't be surprised if there was more underground."
"There's no clear signs of the ark, but the ship is reading intense bursts of energy from underground."
"If they're here, they might have chosen to live underground - perhaps to access water, or to stay safe from the sun."
"In any case, I need to land to recharge the energy core. And I should eat something."
"I locate the region with the strongest signatures: a mountainous area near the planet's north pole."
"I put in the coordinates and carefully steer the ship towards the atmosphere."
"The oranges and reds become even more brilliant as I descend. The mountains look like marble - they're almost psychedelic."
"There's a small strip of flat land ahead. I slow the ship, bring it about, and make my landing."

scene bg mountains
with Dissolve(2.0)

"I push open the hatch and climb out, once I'm sure I'm fully innoculated."
"The sun beats down on me. I can feel myself sweating already. The air smells metallic and faintly of mud."
"I'd want to live underground too, if I landed here."
"I decide to find some shade before anything else."
"The sun is already disorienting me, making me dizzy and dehydrated... this could be bad."
"But there are no trees to be found."
"I wander a ways away from the shuttle, looking for a valley or a river or something -"
"But there's nothing. Just more mountains."
"I squint and try to see something, anything through the piercing sunlight."
"What I see are holes."
"They look tiny in the distance, but as I examine the hills nearby I can see larger ones."
"Now that I see them up close, they don't look like holes anymore."
"They're burrows."
"The thought of fresh water and shade emboldens me, and I frantically search for the nearest one."
"I see one just a few feet away on the next hill. I run for it."
"These burrows are huge. This one must be at least six feet in diameter!"
"I step forward towards it. I bet it leads to an underground river..."
"Maybe Penelope's there. Splashing around, playing in the water. Learning to enjoy warm weather for once."
"I hear splashing inside, too."
"I climb down inside the burrow and follow the sound."

scene bg cave
with Dissolve(2.0)

"The splashing stops."
t "Penelope?"
"I get to the water source. It's a tiny underground lake. Light from outside reflects off of the surface and paints patterns on the ceiling."
"Penelope's in the water."
t "Penelope!"
"She turns to look at me..."
"And she's not Penelope."

show boy neutral

"The creature is as surprised to see me as I am to see it."
"It lets out a shrill scream."
"The sound is high-pitched and grating. My hands rush to my ears to shield them."
"I step backwards and trip over my feet."
"When I look up again there's another creature at the entrance of the cave. This one is larger."
"It enters the cave and scuttles towards me. Its legs are covered by a long skirt, but I can see at least eight of them."
"It strides past me and picks up the smaller one, placing it down by its feet."

show dad angry behind boy

u "We've claimed this cave for our own. Whatever you are, you're not welcome here."
"Somehow, my translator manages to parse out what sound like whistles and trills into something I can understand."
t "I don't mean to claim it. I'm sorry."
t "I was just looking for refuge from the shade."
u "Are you a surfacer? Is that what you look like?"
u "You don't look like you'd survive out there."
t "Yes - I mean, no, I wouldn't. I'm not a surfacer. I'm a traveller."
t "I'm from space."
t "I've come looking for my people. I was separated from them... I just want to know if they're here."
u "Well, they're not."
t "...Alright. I'm sorry for inconveniencing you."
"I look at the smaller one again."
t "Is that your child?"
t "My child is with the others of my people."
t "I'm looking for her too."
t "Are you its mother?"
show dad neutral
d "...I'm his father. His mother's the Queen."
t "Oh, wow. Does that make him a prince?"
"They stare blankly at me."
"It takes me a moment to realize the confusion - they don't mean royalty."
"The translator was thinking of ants."
t "I'm sorry. I just... just nevermind."
pause(1.0)
show dad happy
d "Hear that, son? You're a prince! Ha!"
b "A prince."
d "That would make your sister a princess. Would you get her for me? I think she's still outside."
hide boy
d "How long will you be staying?"
d "I should have enough dinner for you for a week, if need be."
t "What?"
t "I mean - if I'm unwelcome I can leave. I can stay in my ship -"
d "Not at all. Surfacers aren't welcome, but travellers are."
d "Besides, we're just making a home out here. I could use the help."
d "You can build the furniture, make our meals and get things in order."
d "Do those sound like fair terms?"
t "Terms?"
d "Yes. For your stay."
"Sometimes I wish the translator would do more work for me..."
t "I should only stay a couple of nights. Once my shuttle's back in order, I should get back to space."
d "Nonsense! You can stay the week. Fair terms for both parties - sounds like we've got ourselves a hospitality contract."
"Fair terms... I frown, but my expression doesn't seem to translate well either."
hide dad
"Nonetheless, I follow the father's instructions and spend the rest of the day cleaning up the cave."
"The father is courteous towards me, but not very talkative - he seems focused on a dining table he's building, with benches long and narrow enough to accommodate all their legs."
"The chlidren stare at me from across the room, but they're shy. I catch the daughter telling the son that my nose is scary."
"They agree to take on dinner duties for tonight - which is a relief, since I have no idea what is even edible on this planet."
"They seem unbothered by nakedness - the father takes off his skirts when he's inside - so I take a quick break before dinner to soak in the water."
"It's cool and clear. If all I had to do was sit here, this might even be a pleasant planet to live on."
"I get dressed again - much to the son's confusion - when we're called for dinner."
show dad neutral
show son neutral behind dad
d "This is our first night at our new table."
d "What do we say at the table? Maybe our Prince knows something about that?"
b "We stomp on the dirt for refusing us, and we taunt it for taking what we have."
"In unison, they make a high-pitched buzzing noise. The daughter looks a bit mad that I don't partake in this part of the pre-dining ritual."
"I feel like my translator is out of its depth here."
d "Excellent. Now let's dig in."
"I try to tell myself that the slabs of meat in front of me aren't giant worms, but the resemblance is truly uncanny."
"When I take a bite, though, I find them rather tasty."
"Sort of like fish, but with a deep, savory and salty flavor."
"They serve it with what looks like a stick from a shrub. After a bite of that, I decide I've had enough and focus on finishing my worm."
d "So why would anyone go to space?"
d "It seems completely pointless. And uncomfortable."
b "Uncomfortable!"
t "Our planet was destroyed."
t "We had to escape. We're looking for a new home."
d "Huh."
d "Well, you can stay here. You'd have to do a lot of work for a daughter as well, though."
t "I'm not... I'm really - "
t "I mean... we'll figure out the terms of the contract later."
t "For now I just have to find her."
d "Understood."
d "And what do you think of our home?"
t "It's cozy. Comfortable."
show dad happy
d "You think so?"
d "Listen. You're our guest. If you're under contract with us, you have to contribute something to our home."
d "What is your home like? Maybe we can build something like it."
"My first instinct is to describe the ark, but the thought of that hurts for some reason."
"And I don't want to admit that I don't have a home right now."
menu:
   "But there are other homes I could describe..."
   "Like my childhood home.":
      $ childhome = True
      $ newhome = False
      t "My home is in the countryside, just near the mountains."
      t "There are farms and fields nearby, and a small town where I went to school."
      t "We have a garden around back with fruits and vegetables."
      t "The kitchen is really open, with a view of the outside. And there's a big fire pit where we have barbeques when it's warm."
      t "The house always smells like food."
      d "You eat your food outside?"
      d "Doesn't it get too hot?"
      t "Not really. We usually ate - er, {i}eat{/i} outside at night."
      d "And it doesn't get too cold?"
      t "It's not like here. It's very pleasant in the evenings."
      d "I see."
   "Like my dream home.":
      $ newhome = True
      $ childhome = False
      t "My home is on a hill, overlooking a big valley."
      t "It's not too big - just enough for Penelope and I - but there's a deck outside where we can have people over or just sit outside if we want to."
      t "It's near the beach, too. But we have a little pool for hot days."
      d "What's a deck? And what do you do with a pool?"
      t "A pool is like this lake, but it's portable, so you can take it outside."
      t "Usually you just sit in it, or put your feet in. When it's warm, anyways."
      t "And a deck is like an outcropping made of wood that you keep outside."
      d "It doesn't get too cold? Or too hot?"
      d "Wouldn't the wood dry out?"
      t "Not if you keep it in good shape."
      t "And our planet... it's not this. It's not hot like this, and not too cold at night either."
      d "Hmm... alright."
"We finish our food."
d "Was that good, kids?"
b "Yeah!"
"The kids kick the dirt in celebration. The dad does the same."
"I poke at it with my foot, but it just doesn't have the same effect with only one leg."
d "Now that dinner's out of the way, how about dessert?"
b "YEAH!!!"
"He brings out a big bowl of a sweet, viscous liquid."
"All at once, they stick their feelers into it and start slurping it up, leaving me to use my fingers."
"It looks a bit like honey, but it tastes creamy and tangy and a little spicy all at once."
"It occurs to me that it's not this family's differences that are confusing me -"
"It's how similar they are."
if childhome:
   "I think about eating ice cream on the porch with my grandparents when I was little."
   "My parents never gave me extra dessert, but after I went to live with grandma and grandpa, they couldn't help spoiling me even though they were supposed to be my primary guardians."
if newhome:
   "I imagine Penelope sitting here, slurping up the honey along with these kids."
   "She always did like sweet foods."
   "When I see her again, wherever we end up, I'll find her something as delicious as this, and we'll eat it together."
   "Maybe on a deck."
"As soon as we finish the dessert, it's off to bed for the kids - and for me, unexpectedly."
"The dessert had some sort of sedative in it."
"I barely make it to my designated spot in the corner before I'm out like a light."

scene bg black
with Dissolve(2.0)

scene bg mountains
with Dissolve(2.0)

"I feel obligated to stay out the week. In the grander scheme of things, a few days shouldn't make a difference."
"I don't know how homes are supposed to look for this family, but by the time my contract is up, I think this one looks pretty damn good."
if childhome:
   "I'm surprised when the dad remembers the fire pit from my story and asks for help building one the day before I leave."
   "We dig out a hole and organize some stones around it."
   "That night, before it gets too cold, I set up a fire and try my hand at roasting worms."
   "They don't turn out half-bad, which is saying something - I was always a terrible cook."
   "The kids dance around the fire and poke at it with sticks while the dad and I talk more about designing his home."
   "This is nice - almost a little suburban."
if newhome:
   "I'm surprised when, a couple days before I'm scheduled to leave, the dad comes in carrying a huge, long tree, asking me to cut it into a deck for him."
   "I consider explaining that it doesn't work like that, but I give up before I start."
   "Instead, I help him cut the log into long, thin strips, and find the flattest piece of land nearby to lay them flat together."
   "It's as good a deck as I'll make in a day."
   "The next day, the father heads deeper into the cave and emerges with a few sheets of plastic."
   "It takes almost the whole day, but we dig out a section of earth a couple feet deep, line it with the plastic, and fill it with water from the cave, bucket by bucket."
   "By almost the end of the day, we have a deck and a pool."
   "We eat dessert in the sun, my feet dipped in the water while the kids play in it."
   "It's nice - almost a little suburban."
"I wake up the next morning with the son curled up next to me. And when I get ready to leave, he throws a tantrum."

show boy angry
b "You're not leaving! You can't leave!"
if childhome:
   "He kicks in the fire pit until the hole we dug is almost gone."
if newhome:
   "He pulls the plastic sheet out, spilling water all over the deck."
show dad angry behind boy
d "She fulfilled her contract. It's time for her to go."
b "You {i}never{/i} let me have nice things!"
t "Hey, it's alright. You still have your dad."
b "He's not enough!!"
t "Well... maybe I'll be back someday. If I find Penelope, maybe I'll bring her too."
pause(1.0)
show boy neutral
b "Really?"
b "You'll bring her?"
b "Is it a contract??"
t "I, uh..."
"I know how unflappable this family is. It's not worth the fight."
t "Sure. It's a contract."
"The boy jumps for joy, quite the feat with eight legs."
"He scuttles back to his sister and father and hugs them."
show dad happy
d "Thanks for all your help."
t "Just fulfilling my contract."
t "Thank you for welcoming me into your home."
"When I take off in my shuttle, I make sure to circle around a couple of times, just to impress the kids."

scene bg space
with Dissolve(2.0)
"But when I'm back in space, I find myself a little sad."
if childhome:
   "It's pointless to miss my childhood home. By now it's wiped off of the face of the earth, and everyone who knew it is dead."
   "I wouldn't have joined the army in the first place if that weren't true."
   "But I do miss it."
   "Sometimes I wish I could go back to it, somehow."
if newhome:
   "I wonder if Penelope and I will ever have a home like that."
   "Honey and splashing in the pool..."
   "It seems impossibly far from where I am now."
   "But maybe it doesn't have to be."
"I stare up into the emptiness of space, and just for a moment, let myself think of home."

jump space2

label blue1:

"I put in the coordinates for the blue planet."
"The higher temperature variation could mean a higher likelihood for inhabitability."
"...That's what I tell myself, but it feels like I'm reassuring myself more than anything."
"The ship's propulsion systems come to life, and soon I'm accelerating through space watching the stars go by above me."
"Penelope's game broke too."
"I let myself think of her for a moment, but it hurts too much."
"At least if I'm asleep it'll hurt less."
"I'm still not sure how long I'll be asleep, but I put that thought out of my mind and recline my chair backwards."
"I settle my arms into the armrests and feel the needles prick my wrists."
"At the edge of sleep, I still feel like I'm in the water with Calypso."
"I swear I can feel it lapping against my hair."
"It occurs to me that I haven't been dry in a long time..."

scene bg black
with Dissolve(2.0)

p "Mom?"
p "Do you know who my father was?"
p "Can you tell me about him?"
if truth:
   if calypso1:
      t "Your father..."
      t "I don't know they'd want you to call them that."
      t "They told me to forget."
      t "I have to forget."
   else:
      t "Your father..."
      t "I don't know they'd want you to call them that."
      t "They told me to forget..."
      t "But I can't."
      t "I'm so sorry, Penelope. But I can't."

else:
   if calypso1:
      t "Your father..."
      t "Your father is dead."
      t "They told me to forget."
      t "I have to forget."
   else:
      t "Your father..."
      t "Your father is dead."
      t "They told me to forget..."
      t "But I can't."
      t "I'm so sorry, Penelope. But I can't."
p "Why do we have to forget?"
p "Why can't we remember things, mom?"
p "I forget the taste of coriander."
p "I forget what the flowers smelled like."
p "I forget what you looked like."
p "Why do I have to forget?"
p "Why did we never take a photo together?"
p "Mom..."
"I hold Penelope's face in my hands."
if truth:
   "To help her."
else:
   "To comfort her."
"But she has no face."
"She has no face because I have forgotten her face."
"I have forgotten her and she has forgotten me, and she slips from my hands and becomes the waters of Calypso, and they pour over me and fill my ship until everything is dark."

scene bg space
with Dissolve(2.0)

"I feel a terrible weight on my chest."
"The weight wakes me up, but my body refuses to move."
"I try to open my eyes but my lids are so heavy... I can barely keep them open."
"I lie like this for a while. I'm not sure how long."
"The stasis is coming offline."
"My body starts to feel lighter."
"Finally I can move."
"I open my eyes to find that we're about to begin our descent."
"Above me floats the planet."
"The dot on my map was blue, but the surface of the planet is a blend of pinks and yellows, with deep green oceans and massive storms."
"Entire swaths of it are desert yellow, and the poles are dotted with white."
"Calypso was right about the temperature variation."
"I'm distracted from the view by a faint beeping from one of the screens."
"I pull the chair back upwards and examine it."
"The beeping is a beacon from the planet's surface -"
"One of our distress beacons."
"The ark could have landed here. Penelope could have--"
"The ship shudders as we start to hit the planet's upper atmosphere. I turn my attention to the control panel."
"I angle the ship above the planet and punch in the coordinates of the beacon."
"The ship shudders as we hit the lower atmosphere, but it stays steady."
"I look down at the ground. It is a flood of colours: pinks, yellows and greens."
"It looks like a jungle."
"Safer than the desert, I think - but then I realize how low we are to the ground."
"The trees are huge."
"I take control of the ship and decelerate."
"Then, carefully, my eyes fixed on the ship's screens, I lower it into the forest."
"I manage to dodge the tree branches and find a soft landing spot on the forest floor."

scene bg black
with Dissolve(2.0)

"Before I leave the ship, I innoculate myself and eat some preserved foods Calypso left for me."
"I give myself a moment's rest - but I don't need more than that."
"As long as it lasts, the stasis machine has no concept of time. I have no idea how long I've slept."
"All I know is it was more than enough."
"Finally, I open the hatch and emerge out into the jungle."

scene bg jungle-day
with Dissolve(2.0)

"They looked smaller from the shuttle."
"From the ground, the trees are as big and as wide as skyscrapers."
"There are leaves as big as the ship - but most of the trees don't have leaves. Instead they have porous puffs like fungi."
"The fungi rain down spores that coat the forest floor."
"I bring a GPS locator, a few meals' worth of food, and a filter for water. With all of my supplies in order, I begin climbing my way towards the signal."
"It takes twice as much effort to cover half the ground on the forest floor."
"Above me I can hear animals - birds with voices so low that the leaves shudder with the sound waves, the scuttling of what I imagine is some huge insect, the occasional ruffling of one of the giant fungi."
"Down here, though, the animals are mercifully small."
"I'm starting to relax and fall into the rhythms of the walk when something catches my eye up in the canopy."
"It's a spot of sunlight, sunlight that is otherwise blocked by the leaves and spores."
"A tree branch has been torn from a tree, leaving the spot open."
if blue1:
   "It's fresh. This must have happened recently."
if blue2:
   "The tree has started growing back. I don't know how fast anything grows here, so I don't know what that means, but it's not fresh."
if blue3:
   "I barely notice the break - a new branch has almost completely taken its place."
"It's too small to have been caused by the ark."
"My heart sinks."
"But it could still be something. I have to at least look for it."
"I squint up at the crack in the branch and follow the direction it points."
"I shimmy up a root of one of the trees and then climb up a vine until I have a good vantage point."
"Then I look out."

"The wreck of the shuttle is still smoking lightly."
"This one is larger than mine. I recognize it as a fourth class shuttle; it should fit six people, maximum."
"It has more fuel than mine, and even a rudimentary weapons system."
"This must have been an important mission."
"Could the ark be nearby...?"
"I climb back down to the vine and drop from the branch to a large rock, then slide down through the crater."
t "Hello?"
t "Is anyone alive?"
"I take a few steps towards the shuttle and then break into a run."
t "Please be alive... please--"
"I round the corner around the front of the shuttle, and find the source of the smoke."
"Five men are standing in a line. They are awkward and nervous, weapons shaking in their hands."
"Behind them, they have a fire going, meat roasting on it."
"There is a moment when none of us say anything..."
"And then..."
sol "Commander? Commander!"
"They run to me."
show hector young surprised
"The first one stops just short of me."
"I recognize him: his freckles, round cheeks, big nose."
"This was the soldier who made the call over the radio."
"He's awkward as ever. He doesn't know what to do with me."
"He thinks I'm some illusion."
"I put my hands on his shoulders. Only when they get there do I realize they're shaking."
t "Lieutenant Jensen. Hector Jensen. It's so good to see you."
show hector young neutral
h "Commander..."
"His knees buckle and he falls forward. I pull him in and hug him to keep him steady."
"The other soldiers join us, and soon we're all a mess, tears and shivers and garbled hellos."
"It takes us a few minutes to compose ourselves."
"They all recognize me, but I have to be reminded of a couple of them. They're such junior officers. Some of them only joined when they boarded the ark."
"Finally, we seat ourselves around the fire and stoke it, adding a small log for good measure."
t "I see you've found yourselves some local food."
show hector young happy
h "It took a few tests in the shuttle, but we found something we can eat."
h "Believe it or not, the spores are edible too. And a bit like cotton candy, if cotton candy was bitter as hell."
"I laugh at that."
t "How long have you been here?"
show hector young neutral
h "I'm sure you know how hard it is to tell time."
h "If I'm being honest, we have no idea."
h "When we landed here, it'd been about a month since we left you for dead."
t "What happened after that?"
h "We figured you were lost in the debris. Had a funeral. Moved on to this planet."
h "We hit the trees on the way down, busted up the shuttle. But we were all okay."
h "But it seems like something messed with our technology on the way down."
h "The beacon we put out gave false readings. It told the ark that we were dead."
h "We tried to send out a radio signal, but it was too late. The ark left without us."
"I think back to Calypso and the terrible emptiness I felt when they left me behind."
"Hector notices the look on my face."
h "And what about you? What happened to you out there?"
if calypso1:
   t "I landed on the planet in the debris field. By some miracle I didn't die on the way down."
   t "There was a creature living there... it helped me rebuild my ship and get out."
   t "I was lucky to have its help."
else:
   t "I crashed on the planet in the debris field."
   t "I met a creature there... it helped me rebuild my ship, gave me supplies, nursed me back to health."
   t "I was fortunate to have met it."
t "I had no idea of the ark's heading, so I flew here in the hopes I'd rendezvous with it."
h "Wait... your ship still works?"
h "You mean you can get us off this place?"
t "I'm sorry... the ship only fits me."
t "I would take you if I could."
show hector young sad
h "It's alright."
"A painful silence falls over the camp. I don't want to make this worse, but I have to ask..."
t "How did Penelope take it?"
t "My death, I mean."
"Hector meets my eyes, but he only shakes his head."
"A knot forms in my stomach. I hear myself making something like a groan, but I don't feel the sound leave my body."
"I huddle into a ball."
"But I don't cry."
"I won't cry. Not in front of my junior officers."

pause(2.0)

"Finally, I gather my strength and sit up to eat some food."
"When I look back up at the soldiers, they're glancing uneasily at each other."
show hector young neutral
h "Commander... we don't mean to impose, but..."
h "We were hoping we could get your help."
"Hector pauses to form his words, but one of his men interjects before he can continue."
sol "There are monsters in the woods."
sol "They're stealing our supplies."
sol "They're coming for us and we have no idea what to do."
sol "Will you help us? Will you kill them for us?"
show hector young angry
h "Ensign! That's enough."
sol "I... I'm sorry, sir."
show hector young neutral
h "Commander, we don't want you to kill them for us. I apologize."
h "My men think it's appropriate to ask such things of a commanding officer, and that it's alright to abandon first contact principles at the first sign of danger."
show hector young concerned
h "But we're in a difficult situation here, that's the truth of it."
h "We've lost most of our supplies. We're poorly defended out here."
h "They come from the treetops... they climb down and just take what they want."
h "They're huge. If we fought them, they'd crush us."
h "To be honest, we have no idea what to do."
"When I look at the men again, it strikes me how afraid they all look. It looks like they've barely been sleeping."
"I step out away from the fire and survey their area again. Their fire pit is sitting just under an outcropping of rocks, so it's naturally shielded from one side."
"The shuttle, their remaining supplies, and the outcropping sit just below a huge tree branch that cuts across the whole area."
"The shuttle provides them a bit of a defense from the north, as well. But otherwise, they're very much out in the open..."
"Which isn't necessarily a bad thing."
"When I return, they're all looking at me with trepidation, waiting for me to give them my verdict."
show hector young sad
menu:
   "Just giving them advice won't do. I have to say something that sticks with them."
   "Tell them about my time behind enemy lines.":
      $ badspeech = True
      $ goodspeech = False
      t "I don't talk about this much, but I've been where you are."
      t "I spent over a year behind enemy lines. I wasn't always alone, but for months at a time, I was."
      t "I learned more about who I was back there than any superior officer could have told me."
      t "I learned about how complicated life is on the field. About how decisions that seemed simple were anything but."
      if calypso1:
         t "I learned exactly how far I would go to live on for the people I care about."
      else:
         t "I learned what it meant to live on even though all hope was lost. To learn to live with a new reality."
      t "It kills me that you have to live through this like I have."
      t "And I wish I could offer you more than this."
      t "But this is your life now. And you have to trust yourself to live it - to make your own choices. To do what you have to."
   "Tell them about liberating the labour camp.":
      $ goodspeech = True
      $ badspeech = False
      t "When I saw the labour camp, I wasn't sure I had it in me to take it."
      t "I'm sure you imagined me so sure of myself."
      t "The truth is, I was scared shitless."
      t "But I did it. It wasn't easy. I swear, the whole time, I was asking myself why I was even there. What was I thinking?"
      t "But I did it. I did have it in me."
      t "These are the moments when we discover what we're made of."
      t "I know all of you. You were strong enough to leave your home, to leave everything you knew - and not only that, but you were strong enough to join the army, knowing you could end up here."
      t "And here you are. I'm sure you're all scared shitless."
      t "But heroes never feel like heroes. It still surprises me sometimes that people think I'm one."
      if calypso1:
         t "If it means anything, I believe in you. I believe you can survive here. You can make a life here."
         t "And when I bring the ark back to find you, we'll remember you as heroes, as pioneers, as among the bravest of our people."
      else:
         t "But something we often forget is how few people could be where you are right now."
         t "We're lucky. We only see the best of us, and we come to think of that as normal. But you're not normal. You might be terrified, but you're extraordinary."
label after_speech:
show hector young happy
"It looks like I got it right."
"The soldiers are smiling at each other now."
if goodspeech:
   "Their chests are puffed up just a little, their shoulders straighter."
   "Maybe they're starting to feel like heroes."
if badspeech:
   "Their expressions are somber and serious. But they're ready."
   "They look humbled, too. Everyone on the ark knew not to ask me about those times, and they got to hear the story from me."
h "Thank you, Commander."
h "Truly."

scene bg jungle-night
with Dissolve(2.0)

"Now that they're prepared, I get to helping them fortify their camp."
"There's no way we'll cut down the branch above us - not for a long time, anyways - but we manage to cut down a few of the smaller branches poking out from it. That should give the alien creatures less of an advantage in the canopy."
"We dismantle the shuttle and use its hull to make walls around the supplies. By the time we're finished, the supply cache is practically a small house, with only a small hole in the ceiling for smoke to escape and a door."
"We cut the logs from the branches into sharp sticks and make a fence around the camp."
"We forage for more food and have another big fire that night."
"We sing campfire songs I haven't heard since we left Earth."
"And then, when night falls, we wait."
"I offer to keep watch. I've slept a long time, I say, and soon I'll be sleeping again."
"The jungle is deceptively quiet at night. All I hear for some time is the wind and the low, melodic purr of some distant animal - perhaps something like a frog, or a cricket."
"Then I hear the rustling in the trees."
"I hold my breath and stand up against the doorway. I look up for any sign of the creature."
"I hear it search - and its confusion as it finds the cut branches. It pauses to survey the fence."
"Then, with slow, deliberate movements, it climbs across the branch until I can see it."
"Its eyes glow faintly in the dark."
if goodspeech:
   "It glares at me for a long moment - suspiciously, sternly, but with no threat of violence. It knows it won't be so easy anymore."
if badspeech:
   "Our eyes meet for one long moment. It seems confused, like it's studying me but hasn't drawn a conclusion yet."
"Then, heaving a powerful sigh, it returns to the night."
"I let myself breathe again and look at the soldiers."
"Miraculously, the only one who was woken up was Hector; the others must have been so tired that the idea of me keeping watch alone gave them rest."
"Hector is still bleary-eyed, but he seems to understand that we're safe now."
"He nods to me slowly, and drifts back to sleep."

scene bg jungle-day
with Dissolve(2.0)

show hector young happy
h "I don't know how we can thank you, Commander."
h "I don't know what we would have done."
if goodspeech:
   t "You're stronger than you know. You'd have found it in you, I'm sure of it."
if badspeech:
   t "You'd have done what you had to. You'd have found a way."
h "I'm amazed you have so much faith in us."
h "You barely know us."
t "I know... but I've been where you are."
t "And you'll get through it. Like I did."
h "We have one more request to make. If it's alright."
t "Go ahead."
"He produces a small, thick envelope."
show hector young sad
h "When you get back to the ark..."
h "Please give these to our loved ones."
h "You'll see they're each addressed to someone... We don't mean to make trouble for you, but..."
t "Of course I'll deliver them."
t "I'll make sure they read them. And then I'll bring them back here to find you."
t "I promise."
"I hug each of them in turn. It's harder for me to leave them than I'd like to admit."
"But their letters give me hope that I can find my way - that I must find my way."
"With that encouragement, I leave them behind."
"The ship is in working order and ready to go when I return to it."
"Carefully, I navigate through the branches and the canopy, and then I accelerate into the sky."
"I look down one last time at the camp and remember my promise."
"I remember my promise to Penelope, too. In the envelope, pressed between the pages of letters, sits a tiny purple flower."
"Soon the camp is lost beneath the canopy, and then beneath the clouds, and then once again I'm alone in space."

jump space2

label space2:

"The quiet whirr of the energy core and the empty space all around me should make me feel lonely, but somehow I am calmed by it."
"I don't know what that says about me."
"What positivity I have left fades when I return to the map."
"I have two dots left to choose from."

if blue1:
    $ okbreak = False
    $ missyou = False
    $ childhome = False
    $ newhome = False
    "There's a larger planet, almost the same distance from its sun as Earth was from ours. Its sun is a little smaller, so it should be just a little cooler. On the map, it looks like a green dot."
    "And there's a smaller planet closer to its sun. Calypso said that it's supposed to be warm and dry. It's an orange dot on the map."
    "Once again, I have no way of knowing where to go."

    menu:
       "And yet, I must decide."
       "The green dot.":
          $ green2 = True
          $ orange2 = False
          $ blue2 = False
          jump green2
       "The orange dot.":
          $ orange2 = True
          $ green2 = False
          $ blue2 = False
          jump orange2

elif orange1:
    $ okbreak = False
    $ missyou = False
    $ goodspeech = False
    $ badspeech = False

    "There's a larger planet, almost the same distance from its sun as Earth was from ours. Its sun is a little smaller, so it should be just a little cooler. On the map, it looks like a green dot."
    "The other planet rotates on a strange axis. It should have more extreme temperature variations that I'm used to. It's a blue dot on the map."
    "Once again, I have no way of knowing where to go."
    menu:
       "And yet, I must decide."
       "The green dot.":
          $ green2 = True
          $ orange2 = False
          $ blue2 = False
          jump green2
       "The blue dot.":
          $ blue2 = True
          $ orange2 = False
          $ green2 = False
          jump blue2

else:
    $ childhome = False
    $ newhome = False
    $ goodspeech = False
    $ badspeech = False

    "There's a planet that rotates on a strange axis. It should have more extreme temperature variations that I'm used to. It's a blue dot on the map."
    "The other planet is smaller and close to its sun. Calypso said that it's supposed to be warm and dry. It's an orange dot on the map."
    "Once again, I have no way of knowing where to go."
    menu:
       "And yet, I must decide."
       "The blue dot.":
          $ blue2 = True
          $ orange2 = False
          $ green2 = False
          jump blue2
       "The orange dot.":
          $ orange2 = True
          $ blue2 = False
          $ green2 = False
          jump orange2


label orange2:

$ detonate = False
$ killscout = False
$ speakup = False
$ stayquiet = False

"I punch in the coordinates for the orange planet."
"A warmer planet might be more promising for settlement..."
"It's a slim chance, but I'll have to take it."
"I engage the ship's engines and watch the stars turn to blurry lines out the window."
"Penelope always preferred the cold."
"She was a weird kid like that."
"I suppose she never got to do anything fun in the heat, so for her it was just uncomfortable."
"She never got to go to the beach on a hot summer's day, or take a nap in the warmth of the sun..."
"If she had, would she still prefer the cold?"
"Or is she sitting on that planet right now, feeling uncomfortable and grumpy that of all the planets in the galaxy, they had to pick the hot one?"
"I wouldn't have let them pick the hot one, I think as I recline the chair and slip my arms into the armrests."
"Even if we had to go it alone, I would have made sure we built our home somewhere she liked."
"The thought lingers with me as I drift into stasis."

scene bg black
with Dissolve(2.0)

p "You never talk about where you grew up."
p "Did you live in a bunker too?"
p "Did you have a garden?"
p "What were you like before you had me?"
if goodspeech:
   t "I was a hero."
   t "To the world, I was invincible..."
   t "And I never let anyone in."
   p "You're right..."
   p "You don't let anyone in."
   p "You never let me in."
   p "You were my hero, but were you my mother?"
if badspeech:
   t "I was pragmatic."
   t "I did what I had to do to survive."
   p "What about me?"
   p "To have a child in the middle of that..."
   p "I wasn't what you had to do."
   p "But you made me."
   t "You were different."
   p "Was I?"
   p "Or was I just something you used to pull yourself out?"
if simplicity:
   t "I was a problem-solver."
   t "I was happiest when I could solve the most."
   t "I felt like I was doing something."
   p "You mean you were a simple problem-solver."
   p "You hate anything that's complicated."
   p "You love me now that I'm a simple problem."
   p "Find Penelope. Save Penelope."
   p "But when I was right in front of you, I was too complicated."
if danger:
   t "I was a thrill-seeker."
   t "People like to think of me as some solemn hero..."
   t "But I liked the violence."
   t "I liked being in danger."
   p "And you hated safety."
   p "You hated the ark."
   p "You hated coming home to me every night."
   p "You only had me because your pregnancy was so dangerous."
if childhome:
   t "I was a stupid kid from the country."
   t "All I wanted was to protect my family..."
   t "But my family died. My whole town died."
   p "They had to die, didn't they?"
   p "For you to live."
   p "If it weren't for them, you would have died a stupid kid."
   p "You're grateful they died. You wanted them to die."
   p "It should have been you, not them."
if newhome:
   t "I was naive."
   t "I thought I would live a quiet life..."
   t "I thought I could make a new home."
   t "A new home with you, Penelope."
   p "That's never what you wanted and you know it."
   p "You're still naive."
   p "You're naive because you think you're any smarter than you were back then."
p "I hate you, mom."
p "No..."
p "I don't even know you."
p "You're not my mother."

scene bg space
with Dissolve(2.0)

"I wake up to a red glow."
"Is it sunlight?"
"How long was I napping for? Is it sundown already?"
"I open my mouth to call to my grandma."
"Please tell me I didn't oversleep again..."
"But I didn't oversleep. The stasis pod always wakes me up ontime."
"No, the red glow is from the planet, hovering above me."
"It's almost entirely orange and red - deserts lined with oxidized iron, from the looks of it."
"Lines of green and blue slice and swirl across it. So it must have some fresh water. I wouldn't be surprised if there was more underground."
"There's no clear signs of the ark, but the ship is reading intense bursts of energy from underground."
"If they're here, they might have chosen to live underground - perhaps to access water, or to stay safe from the sun."
"In any case, I need to land to recharge the energy core. And I should eat something."
"I locate the region with the strongest signatures: a mountainous area near the planet's north pole."
"I put in the coordinates and carefully steer the ship towards the atmosphere."
"The oranges and reds become even more brilliant as I descend. The mountains look like marble - they're almost psychedelic."
"There's a small strip of flat land ahead. I slow the ship, bring it about, and make my landing."

scene bg mountains
with Dissolve(2.0)

"I push open the hatch and climb out, once I'm sure I'm fully innoculated."
"The sun beats down on me. I can feel myself sweating already. The air smells metallic and faintly of mud."
"I'd want to live underground too, if I landed here."
"I decide to find some shade before anything else."
"The sun is already disorienting me, making me dizzy and dehydrated... this could be bad."
"But there are no trees to be found."
"I wander a ways away from the shuttle, looking for a valley or a river or something -"
"But there's nothing. Just more mountains."
"I squint and try to see something, anything through the piercing sunlight."
"What I see are holes."
"They look tiny in the distance, but as I examine the hills nearby I can see larger ones."
"Now that I see them up close, they don't look like holes anymore."
"They're burrows."
"The thought of fresh water and shade emboldens me, and I frantically search for the nearest one."
"I see one just a few feet away on the next hill. I run for it."
"These burrows are huge. This one must be at least six feet in diameter!"
"I step forward towards it. I bet it leads to an underground river..."
"Maybe Penelope's there. Splashing around, playing in the water. Learning to enjoy warm weather for once."
"I hear splashing inside, too."
"I climb down inside the burrow and follow the sound."

scene bg cave
with Dissolve(2.0)

"The splashing stops."
t "Penelope?"
"I get to the water source. It's a tiny underground lake. Light from outside reflects off of the surface and paints patterns on the ceiling."
"Faintly, I can see objects in the deeper caves. Furniture?"
"But I don't have time for that - "
"Penelope's in the water."
t "Penelope!"
"She turns to look at me..."
"And she's not Penelope."

show boy neutral

"The creature is as surprised to see me as I am to see it."
"It lets out a shrill scream."
"The sound is high-pitched and grating. My hands rush to my ears to shield them."
"I step backwards and trip over my feet."
"When I look up again there's another creature at the entrance of the cave. This one is larger."
"It enters the cave and scuttles towards me. Its legs are covered by a long skirt, but I can see at least eight of them."
"It strides past me and picks up the smaller one, placing it down by its feet."

show dad angry behind boy

"Then it rushes me."
"It's smaller than me, but surprisingly strong. It pushes me up against the wall."
"My ears ring with the impact."

u "{i}Did you take her?{/i}"
u "{i}Did you take my daughter, you surface freak?{/i}"
t "What? No! I..."
u "If you took her I am going to rip you into pieces and feed you to my worms!"
t "I swear, I didn't! I swear!"
t "I just got here! I'm not from the surface, I'm from space?"
u "From space...?"

show dad worried

u "If it really wasn't you..."
u "You trespassed in my home. By rights, I can kill you."
d "But as a father, I don't want my children seeing something like that."
show dad angry
d "So I hereby place you under contract. You are not permitted to leave until one of us finds my daughter."
d "If you try to leave I will shoot you out of the sky."
t "And when we find your daughter I can go?"
d "Yes."
t "Alright."
"It doesn't look like I have a choice."
scene bg mountains
with Dissolve(2.0)
"He at least lets us wait until the sun's gone down a bit before we start our search."
"He leaves his son at home and we split up."
"He calls for her with a high-pitched buzzing that I can't imitate, and that my translator doesn't understand."
"Instead, I search quietly, for the most part. When I'm near a cliff or a cave, I holler, and wait for a response."
"All I find is echoes."
scene bg cave
with Dissolve(2.0)
"When I start to have trouble seeing in front of me, I return to the cave."
show boy angry
b "You're not supposed to be back yet."
t "I'm sorry, I..."
b "You're under contract."
b "You know what happens if you break the contract?"
t "I physically can't look anymore! I'm not breaking any contract!"
b "FIND MY SISTER!"
"He pushes me out of the cave. He's strong like his father."

scene bg black
with Dissolve(2.0)

"I walk a little ways off, but I don't want to get lost, so I stop and wait."
"I'm contemplating what to do next when the father comes back."
show dad worried
t "Any sign of her?"
d "Nothing."
"He looks utterly defeated."
"Tentatively, I reach out and touch his shoulder."
"the touch surprises him, but he doesn't object."
t "I'm sorry."
t "I have a daughter too."
t "I was separated from her... I'm looking for her now."
t "That's why I'm alone."
d "If you'd told me that a few days ago, I'd have asked how you could possibly have let her out of your sight."
show dad sad
d "Now, I..."
t "I know. You think you know exactly what you'd do, but then they're gone, and everything changes."
if truth:
   t "I like to think that Penelope can make it on her own."
   t "I raised her to be strong."
   t "It still hurts like hell, but that thought gets me through the days, if nothing else."
   t "It's the same for you. Just remember how you raised her."
else:
   t "It makes me sick just to think of her now."
   t "How terribly alone she must feel..."
   t "All I can do is make sure I get back to her as soon as I can."
   t "It's the same for you. Just do what you can."
"It's hard to tell if my words helped him."
"But he does straighten his back a little, and starts walking back to the cave."
d "We should turn in for a few hours. We can start the search again just before sunrise."
hide dad
"We barely manage to sleep."
scene bg cave
with Dissolve(2.0)
"When we wake up, the dad offers me a modest breakfast: some sort of dried meat, sour, pungent berries, and what looks like porridge but tastes like dragonfruit."
"I'd forgotten how hungry I was. I wolf the meal down despite some small protests from my stomach."
"While we eat, the boy goes out to look himself."
"Meanwhile, the dad and I decide to split up again."
scene bg mountains
with Dissolve(2.0)
"I climb across the hills and call out a few times, but I give up when I realize that I might be scaring the daughter away."
"So I quiet down and soften my footfalls."
"I come to a steep hill just out of sight of the cave."
"I have to get on my hands and knees to climb all the way up."
"I peek over the top."
"The first thing I see is a leg."
"The hillside is spattered with black blood that puddles around the leg and leads in a trail down the other side of the hill."
"I climb over the hill and make my way down along the trail."
"I turn a corner."
"The girl's body is lying down between two trees."
"Her eyes are swollen shut. She's missing a few of her legs."
"The smell almost makes me throw up on the spot."
"She smells like meat cooking in the sun."
"She's been dead a while."
"I'm so repulsed by the sight that I almost don't notice her brother hiding behind a rock."
show boy neutral
t "What are you doing here?"
t "Did you just... did you just find her like this?"
"The boy stares at me blankly."
"He doesn't share my shock."
t "What did you do...?"
b "She broke our contract."
b "I told her it was a contract. I told her what would happen."
b "But she broke it."
"I remember his strength and grab for my gun."
t "We have to go talk to your dad now, okay? We have to..."
show boy angry
b "I'm not apologizing!"
b "I'm not, I'm not, I'm not! She did this!"
b "She broke the contract, and {i}we have to keep our contracts!!{/i}"
b "Dad said so!"
d "What did dad say?"
show dad worried behind boy
show boy neutral
"I lock eyes with the boy for just a moment, and watch his expression change from anger to fear to sadness as his father approaches."
"What I don't see is guilt."
"But he's barely Penelope's age..."
"Does he even understand she's dead?"
d "Whose leg is that...? Where's my daughter?"
d "What happened? Son? What happened?"
"I take a couple of steps back and let him past me."
"I can hardly watch the revulsion on his face when he discovers the body."
"He lets out a trill that stings my ears."
"His legs start to shake, and he falls into a clump on the floor."
d "How did this - oh... ugh..."
"All he can do is cry out in pain."
"I've done what they asked. I don't feel welcome anymore."
"But there remains the issue of the boy."
"He's watching me now, wondering what I'll do. Carefully, I step to the side so his father is between us."
"If I'm going to do something, I have to do it now."
"But he looks nothing less than destroyed. What good would it do to tell him his son is a murderer...?"
menu:
   "I decide to..."
   "Tell the father the truth.":
      $ inform = True
      $ keepsecret = False
      t "I'm so sorry. I found her like this, and I found... I found him with her."
      show dad angry
      d "What...?"
      t "He told me she broke the contract."
      t "I don't know what that means. I'm so sorry."
      "He looks up at his son."
      d "Is this true?"
      b "Dad, you told me about the contract. You {i}told{/i} me!"
      b "I was just doing what you told me to!"
      "All the life is gone from the father's eyes when he looks at me."
      d "Your contract is done."
      d "Just... just go."
      t "I'm really -"
      d "{i}Go.{/i}"
      "Reluctantly, I back up and leave them alone."
      "Just as I make it to the shuttle, I hear a sound so high-pitched and so painful that I have to cover my ears."
      "When I fly over them in the shuttle, they haven't moved."
      scene bg space
      with Dissolve(2.0)
      "I try to touch the controls, but my hands are shaking."
      "I can still see the girl, but when I remember her, she looks like Penelope, and I have to stop myself from throwing up."
      "But the boy is Penelope too, in my mind's eye."
      "The boy is Penelope and it's me she's cutting into."
      "I've broken the contract... I've broken the contract and this is what I get."
      "I swear to never think of this again. I'll never have to; the planet's already gone from my field of view."
      "But even as I return to the map, I can't get rid of the pit in my stomach."
      jump space3

   "Cover for the son.":
      $ inform = False
      $ keepsecret = True
      t "I am so so sorry. I found her like this..."
      t "I have no idea what happened."
      t "Your son got here just after I did."
      t "I'm so terribly sorry..."
      "He hides his head in his hands."
      d "Son... come here..."
      "The boy looks at me for a moment, but only a moment."
      "Then he turns to his dad."
      "Silently, he walks to him and hugs him."
      d "I'm so sorry you had to see this."
      d "I'm so, so sorry."
      "His words become cries. The boy doesn't cry, but he holds his dad tighter."
      "Gradually, they fall silent."
      "I leave them alone and return to my shuttle."
      "When I get there, I have to force myself not to throw up."
      "The image of the girl's body creeps into the back of my eyelids, and even when the planet is a tiny red dot in the distance, I feel like I'm still standing there."
      "I'm looking him in the eye and telling him I'll lie for him..."
      "And I'm cutting the girl's throat myself."
      "I ball my hands up into fists and scream as loudly as I can."
      "Then I swear never to think of this again."
      "My stomach is still turning, and my hands are shaking..."
      "But I have to return to the map."
      jump space3

label green2:

$ inform = False
$ keepsecret = False
$ speakup = False
$ stayquiet = False

"I type in the coordinates for the green planet."
"It looks like it would harbor the most similar climate to Earth, given the distance to its sun..."
"I'll take that small hope. It's better than nothing."
"The ship lurches forward, and then the stars are a blur all around me."
"I watch them go by for a while. I look at the screens one by one. I examine the control panels, trace out the alien lettering on my chair, and poke at the innoculation machine."
"I do anything to avoid stasis for just a few more minutes."
"But then my mind wanders to Penelope."
"What is she thinking right now? Does she miss me?"
"What does she think about when she thinks about me?"
"My stomach ties itself in knots."
"I recline my chair and press my arms into the armrests."
"I let the needles prick me and imagine myself staring up at the sky from solid ground, on a planet with fresh air and clean water where I can make a home."
"Is that planet Earth? Is it Calypso? Or is it a place I'll never find?"
"The thought haunts me as I drift away."

scene bg black
with Dissolve(2.0)

p "You never talk about where you grew up."
p "Did you live in a bunker too?"
p "Did you have a garden?"
p "What were you like before you had me?"
if goodspeech:
   t "I was a hero."
   t "To the world, I was invincible..."
   t "And I never let anyone in."
   p "You're right..."
   p "You don't let anyone in."
   p "You never let me in."
   p "You were my hero, but were you my mother?"
if badspeech:
   t "I was pragmatic."
   t "I did what I had to do to survive."
   p "What about me?"
   p "To have a child in the middle of that..."
   p "I wasn't what you had to do."
   p "But you made me."
   t "You were different."
   p "Was I?"
   p "Or was I just something you used to pull yourself out?"
if simplicity:
   t "I was a problem-solver."
   t "I was happiest when I could solve the most."
   t "I felt like I was doing something."
   p "You mean you were a simple problem-solver."
   p "You hate anything that's complicated."
   p "You love me now that I'm a simple problem."
   p "Find Penelope. Save Penelope."
   p "But when I was right in front of you, I was too complicated."
if danger:
   t "I was a thrill-seeker."
   t "People like to think of me as some solemn hero..."
   t "But I liked the violence."
   t "I liked being in danger."
   p "And you hated safety."
   p "You hated the ark."
   p "You hated coming home to me every night."
   p "You only had me because your pregnancy was so dangerous."
if childhome:
   t "I was a stupid kid from the country."
   t "All I wanted was to protect my family..."
   t "But my family died. My whole town died."
   p "They had to die, didn't they?"
   p "For you to live."
   p "If it weren't for them, you would have died a stupid kid."
   p "You're grateful they died. You wanted them to die."
   p "It should have been you, not them."
if newhome:
   t "I was naive."
   t "I thought I would live a quiet life..."
   t "I thought I could make a new home."
   t "A new home with you, Penelope."
   p "That's never what you wanted and you know it."
   p "You're still naive."
   p "You're naive because you think you're any smarter than you were back then."
p "I hate you, mom."
p "No..."
p "I don't even know you."
p "You're not my mother."

scene bg space
with Dissolve(2.0)

"I wake up a little at a time, and then all at once. I gasp sharply and open my eyes with a start."
"I feel as if I've almost drowned, but my body isn't starved for air."
"Suddenly full of a jittery, fearful energy, I pull my chair forward."
"The planet is dead ahead."
"When I first look at it, I have to convince myself that I haven't returned to Earth."
"Its continents are larger, yes, and they're different shapes - but the bright greens and calm blues, cut across by languid clouds..."
"It's like home."
"As we pull in, there is one distinct difference:"
"This planet has scars."
"Some of them are from mining, but from the looks of it, vast tracts of this land were once covered in cities and factories."
"But the cities are dark."
"Even from up here it's clear they've been long abandoned."
"I turn back to my screens. They're reading no beacons or signals from the ark..."
"But I'm low on food, and my energy core's readings are fluctuating dangerously."
"It needs a rest. So I have to land."
"I pick a spot that looks as clear as possible of the cities and structures that litter the planet's surface."
"The ship makes a smooth landing just near what looks like a forest."

scene bg field-day
with Dissolve(2.0)

"When I open the hatch, I find myself at the edge of a vast field."
"Hills roll on as far as I can see."
"The sky is dotted with tiny puffy clouds."
"In the distance, I can just barely see the tips of buildings."
"They must have been magnificent once. But even from here I can see that they're dilapidated."
"On a hill far away, there's a herd of some sort of animal - I can't really see them from here, but it looks like they're grazing. But besides them, I'm alone."
"I gather my gear, step out and close the hatch behind me."
"I sit down in the grass and lean back on my hands."
"It's softer than on Earth. It feels like a pillow."
"The air is clear and smells faintly sweet."
"This is pleasant... and pleasant is something I haven't felt in a while."
"I should look for some food. If that innoculation machine did its job right, it should be safe. And I'll need to eat something before I go back into stasis."
"But for now, I decide to just take in the moment."

pause(1.0)

"After a spot of cloudwatching I pick myself up and head to the forest to forage for some food."
"I'm lucky - I find some mushrooms that test negative for toxins, and I discover that the grass actually tastes delicious, kind of like garlic."
"I even manage to hunt and catch a chubby little creature that looks a bit like a bird."
"I make a fire and cook up my meal."
"I've never been a great cook, but I'm proud of it, if I do say so myself."

scene bg field-night
with Dissove(2.0)

"By the time I finish up and snuff out the fire, it's nighttime."
"I make sure I have all of my things and head back towards the ship."
"Maybe I'll sleep on the grass tonight and head out tomorrow."
"Just as I'm planning my day before I leave, I catch sight of something bright in the fields."
"Fire."
"I drop to the ground and crawl along it to a tree just near the clearing, but out of the way enough that I should be hidden from view."
"There are at least three hundred figures."
"They look like the animals I saw before on the field..."
"But they're wearing clothes. Clearly they're not herding animals."
"How did I not notice that before?"
"They look like they're trying to decide what to do with the shuttle."
"This is bad."
"My translator won't work from here, so all I hear is hissing, clicking and a couple of growls."
"But it's obvious that the fight is getting heated."
"Finally, they seem to come to some sort of agreement."
"One of them, apparently the leader, gives a final, resounding click, and the group disperses."
"A group of about twenty of them set about moving the shuttle. I don't at all believe that they'll do it, but to my surprise, they manage to pick it up and move it down the hill."
"With impressive efficiency, the others take to pitching tents and setting up a camp."
"In just a few minutes, the field transforms into a city before my eyes."
"It's just dark enough now that I feel safe climbing up a tree a little ways back from the edge of the forest. From a safe and secluded spot about halfway up, I scan the tent city."
"There are smaller, interconnected tents that appear to be residential; the larger tents, for the most part, serve some sort of public purpose."
"I see what looks like an infirmary, a dining tent, and a tent especially for children."
"This really is a city."
"Another light catches my eye, and I follow it and find another camp off in the distance. That one looks almost ten times larger."
"I can't see very well in this light, but the structures look more permanent over there."
"I'll have to watch the camp for a weak spot - but there's no way I'm going to make an escape tonight."
"They're probably still looking for me."
"Just as the thought occurs to me, I see a small squadron of the aliens amassing near the shuttle."
"These ones are stockier than the others, with broad shoulders and angry faces."
"The whole species looks like it was made to run, but these ones in particular look like they were built for fighting."
"I drop from the tree and follow the edge of the forest away from the camp until I'm clear of it."
"Then I climb another tree - one that looks solid enough to hold me for a while - and nestle into a spot between two branches."
"There, I watch over the camp as best I can, but my eyelids start to droop."
"Sleep would be a better use of my time now."
"I use a rope from my bag to tie myself to the tree. When I'm sure I'm secure, I drift off into anxious, restless half-sleep."

scene bg field-day
with Dissolve(2.0)

"I wake up early and untie myself from the tree."
"First I look for the squadron from the previous night - but it seems like they've given up for now, or they're searching farther afield."
"I shimmy down the tree and find another one closer to the camp with a better view."
"When I get to the top of it, I find the camp again in turmoil."
"I can't hear them, but they're pointing at the other camp frantically. A couple of the children are crying."
"One of the stockier ones pushes the leader, and two others push him back."
"It's really getting heated."
"I'm so focused on the drama in town that I don't hear the footsteps until they're almost right below me."
"When I finally see them, I almost jump out of the tree."
"I catch myself and crouch down behind some leaves."
"Luckily, they didn't notice me."
"They're carrying a bag. They open it and empty its contents onto the ground."
"I don't recognize any of the technology, but it looks like complicated stuff."
"Maybe this is an engineer of sorts?"
"I don't want to attract attention, so I have no choice but to watch this one with their strange tinkering for a while."
"They're taller and more lithe than the others; their face is thinner, almost aerodynamic."
"They look very angry and very focused."
"Whatever their doing completely engrosses them..."
"Until they finish the task a few hours later."
"They pack up the contents of their bag and get ready to leave."
"And just as I think I'm safe, they look up straight at me."
u "You can come down now."
"Dammit."
"I jump down from the tree and make a soft, clean landing nearby."
show scout angry
"This one hasn't called for the others, I realize. It's still just the two of us, and the fight in the town is still going on somehow."
u "You're the owner of that shuttle, am I right?"
t "Yes."
u "And you've got a translator... I'm betting whatever else you've got in that ship, my people are going to want."
u "You'll have to get out of here soon if you want all your tech intact."
t "I wasn't planning on staying long... but why are you telling me this? Who are you?"
s "I'm a scout."
t "Oh."
s "You're a traveller. Now we know each other."
show scout suspicious
s "And you're right - I could walk back to camp and tell them about you."
s "But then you'd just tell them about what you saw me doing in the forest. That's too much at stake just to rat you out."
t "Thanks... I guess."
s "Just because I'm being nice to you doesn't mean they'll be as nice."
s "We've had others like you before. We used to be nicer..."
s "But things are dire now. We're at war."
s "Now my leader does whatever he thinks is necessary to keep his people safe. And he's desperate."
t "I understand. And I believe you."
t "So what now? Is this just mutually-assured destruction?"
s "Ideally, I'd like something mroe than that."
s "I need you to do me a favour, and I promise I'll do something for you in return."
s "Tonight, you're going to make a run for your shuttle."
s "I'll make sure you don't meet any trouble on the way there."
s "Once you get to it, will you be able to take off safely?"
t "I should, yes."
s "Good."
"They take a small parcel from the bag and hand it to me."
s "I need you to unwrap this and place it on the ground just before you leave. That's all."
t "Can I ask what this is for?"
s "That's not part of our plan."
s "This is what's on offer - you get out, your shuttle stays intact, you leave and don't look back."
s "Is that a deal you can agree to, traveller?"
"There's something about this plan that bothers me..."
"But they're right. This is the best option I have if I want to make it away with my ship."
t "...Yeah, alright. It's a deal."
"I step back and scan the area for another tree to climb."
"But despite myself, before I can get away from the scout, my stomach grumbles."
show scout curious
s "What was that noise?"
t "It was nothing... it's just what happens when I don't eat for a little while."
show scout happy
s "What biological function does that even serve?"
"They make a hissing sound that my translator can't parse out."
"I think it's laughter."
s "Here. I have some extra food."
"They rifle through a bag on their back and pull out a couple of parcels wrapped in fabric."
"They hand one to me."
"It sort of resembles a sandwich. The bread is almost like phyllo pastry: paper-thin leaves, oil and flour in light layers."
"In the middle is tangy-smelling, marinated meat."
"I dig in."
"The first bite makes my stomach turn a little, but I'm so happy to finally have food that I ignore it."
show scout curious
"I finish the whole thing in a few bites and wipe the crumbs from my face."
"When I look up, the scout looks a little surprised."
s "I didn't think you'd shovel the whole thing down right in front of me."
t "I'm sorry. Is that impolite?"
"I neglect to mention that it's impolite for my own culture."
s "It doesn't matter."
s "What I'm more curious about is why you're here at all."
t "I'm looking for my people."
t "We were travelling, looking for a new home... I got left behind."
show scout neutral
s "I'm so sorry."
"Their kindness catches me off-guard."
s "I haven't been off this planet..."
s "But I know what it's like to be left behind."
t "Thanks."

scene bg field-night
with Dissolve(2.0)

"The camp is utterly silent."
"When I descend from one of my trees, I find the scout waiting for me."
show scout neutral
s "Are you ready? Do you have everything?"
t "Yes."
s "Excellent."
s "I'm going to go down first. There's going to be a bit of noise... that's when you make a run for it."
s "Get to the shuttle, unwrap the parcel, put it down, get in and get out."
s "Sound good?"
t "Sure. Let's do it."
hide scout
"They take off in a sprint and bound down the hill to the left of the camp."
"They must be going at least twice as fast as my top speed. It's incredible to watch."
"I lose sight of them as they hit the town."
"I hear some rustling coming from one of the tents. Was that the signal?"
"I hold my breath, waiting for more noise."
"The tents go quiet again..."
"And then I hear screams."
"That's when I see the smoke."
"I want to help them, but I have no time now."
"I take off running out of the forest and down the hill, past a couple of tents and straight to my shuttle."
"There's more smoke now. It stings my eyes as I tear the parcel open."
"I take the object out and crouch down to set it on the ground, as the scout instructed."
"But when I touch it with both hands, I realize how familiar this looks."
"This is a bomb."
"It's large enough that it could take out at least ten of the tents."
"The large tents are all near here: the infirmary, the nursery..."
"I stop. The bomb freezes in my hands."
s "Are you giving up on me now, traveller?"
show scout suspicious
"They circled back to make sure I did the job."
t "I know what this is. I know what you're planning to do."
s "And what does it matter to you?"
t "It matters because - because these are lives we're talking about! They're not my people, but they don't deserve to die like this!"
show scout angry
s "You have no idea what they deserve."
s "You know there used to be three thousand of us?"
s "They all died in the war. A war that the leaders of this flock refuse to let end."
s "So I'm ending it."
t "I won't be a part of this."
s "You don't have to."
s "Just give it to me and I'll do the rest. You won't even see it. You'll be in space before it goes off."
s "But don't take it with you, or you'll rain back down on our field in pieces."
s "And don't think about staying here to work this out. You stay, your shuttle blows up with the tents."
"They're right. I know nothing about this planet or its history..."
"I only know my own planet's history."
"This isn't right."
"But it my place to do something about it?"
menu:
   "My gun is in its holster on my leg... and the scout is eyeing me hopefully."
   "Shoot them.":
         $ killscout = True
         $ detonate = False
         jump shoot_scout
   "Put down the bomb.":
         $ detonate = True
         $ killscout = False
         jump bomb_scout
label after_shoot:

label shoot_scout:

"In a fluid motion, I grab my gun from my holster and flick it upwards."
"The scout sees it at the last moment."
"They lunge forward."
"They make it almost right to me before I take the shot."
"I take another, and another."
"They fall back and slump to the ground."
hide scout
"Carefully, I lay the bomb down on the ground. It's still unarmed."
"I breathe a sigh of relief and open the hatch."
"I'm about to climb in when I look up to find the leader staring at me."
"Their eyes move from the scout's body, to the bomb, to me."
t "I'm so sorry."
"They don't say anything, but they seem to understand."
"I've seen all I want to see. I leap into the hatch, close it behind me and slam on the accelerator before I've even settled into my seat."
"I grab onto the chair as we hover above the ground and launch into the sky."
"I don't even get the chance to look back."

scene bg space
with Dissolve(2.0)

jump space3

label bomb_scout:

t "I'll arm it."
t "That'll give you enough time to escape the blast radius."
show scout neutral
s "Thank you."
"The scout steps back."
s "I hope you find your people."
"Taking a deep breath, I look down at the bomb."
"I hope I'm making the right choice."
"I press the button and it lights up."
"I dash to the shuttle, open the hatch and dive inside."
"As I close it, I see the leader of the camp emerge from one of the tents."
"Our eyes meet."
"They look at me, then at the bomb, and I see the realization dawn in their eyes just as the shuttle lifts off."
"By the time the bomb goes off behind me, I'm safely in the air."
"I circle around to look at the destruction. I let the image burn into my eyes."
"But it's the leader's face that stays with me as I push through the atmosphere into space."
scene bg space
with Dissolve(2.0)
"I take a moment to hover in the silence and think about what I've just done."
"Then, with everything I have, I push it out of my mind."

jump space3

label blue2:

$ inform = False
$ keepsecret = False
$ detonate = False
$ killscout = False

"I put in the coordinates for the blue planet."
"The higher temperature variation could mean a higher likelihood for inhabitability."
"...That's what I tell myself, but it feels like I'm reassuring myself more than anything."
"The ship's propulsion systems come to life, and soon I'm accelerating through space watching the stars go by above me."
"Penelope's game broke too."
"I let myself think of her for a moment, but it hurts too much."
"At least if I'm asleep it'll hurt less."
"I'm still not sure how long I'll be asleep, but I put that thought out of my mind and recline my chair backwards."
"I settle my arms into the armrests and feel the needles prick my wrists."
"At the edge of sleep, I still feel like I'm in the water with Calypso."
"I swear I can feel it lapping against my hair."

scene bg black
with Dissolve(2.0)

p "You never talk about where you grew up."
p "Did you live in a bunker too?"
p "Did you have a garden?"
p "What were you like before you had me?"
if goodspeech:
   t "I was a hero."
   t "To the world, I was invincible..."
   t "And I never let anyone in."
   p "You're right..."
   p "You don't let anyone in."
   p "You never let me in."
   p "You were my hero, but were you my mother?"
if badspeech:
   t "I was pragmatic."
   t "I did what I had to do to survive."
   p "What about me?"
   p "To have a child in the middle of that..."
   p "I wasn't what you had to do."
   p "But you made me."
   t "You were different."
   p "Was I?"
   p "Or was I just something you used to pull yourself out?"
if simplicity:
   t "I was a problem-solver."
   t "I was happiest when I could solve the most."
   t "I felt like I was doing something."
   p "You mean you were a simple problem-solver."
   p "You hate anything that's complicated."
   p "You love me now that I'm a simple problem."
   p "Find Penelope. Save Penelope."
   p "But when I was right in front of you, I was too complicated."
if danger:
   t "I was a thrill-seeker."
   t "People like to think of me as some solemn hero..."
   t "But I liked the violence."
   t "I liked being in danger."
   p "And you hated safety."
   p "You hated the ark."
   p "You hated coming home to me every night."
   p "You only had me because your pregnancy was so dangerous."
if childhome:
   t "I was a stupid kid from the country."
   t "All I wanted was to protect my family..."
   t "But my family died. My whole town died."
   p "They had to die, didn't they?"
   p "For you to live."
   p "If it weren't for them, you would have died a stupid kid."
   p "You're grateful they died. You wanted them to die."
   p "It should have been you, not them."
if newhome:
   t "I was naive."
   t "I thought I would live a quiet life..."
   t "I thought I could make a new home."
   t "A new home with you, Penelope."
   p "That's never what you wanted and you know it."
   p "You're still naive."
   p "You're naive because you think you're any smarter than you were back then."
p "I hate you, mom."
p "No..."
p "I don't even know you."
p "You're not my mother."

scene bg space
with Dissolve(2.0)

"I feel a terrible weight on my chest."
"The weight wakes me up, but my body refuses to move."
"I try to open my eyes but my lids are so heavy... I can barely keep them open."
"I lie like this for a while. I'm not sure how long."
"The stasis is coming offline."
"My body starts to feel lighter."
"Finally I can move."
"I open my eyes to find that we're about to begin our descent."
"Above me floats the planet."
"The dot on my map was blue, but the surface of the planet is a blend of pinks and yellows, with deep green oceans and massive storms."
"Entire swaths of it are desert yellow, and the poles are dotted with white."
"Calypso was right about the temperature variation."
"I'm distracted from the view by a faint beeping from one of the screens."
"I pull the chair back upwards and examine it."
"The beeping is a beacon from the planet's surface -"
"One of our distress beacons."
"The ark could have landed here. Penelope could have--"
"The ship shudders as we start to hit the planet's upper atmosphere. I turn my attention to the control panel."
"I angle the ship above the planet and punch in the coordinates of the beacon."
"The ship shudders as we hit the lower atmosphere, but it stays steady."
"I look down at the ground. It is a flood of colours: pinks, yellows and greens."
"It looks like a jungle."
"Safer than the desert, I think - but then I realize how low we are to the ground."
"The trees are huge."
"I take control of the ship and decelerate."
"Then, carefully, my eyes fixed on the ship's screens, I lower it into the forest."
"I manage to dodge the tree branches and find a soft landing spot on the forest floor."

scene bg black
with Dissolve(2.0)

"Before I leave the ship, I innoculate myself and eat some preserved foods Calypso left for me."
"I give myself a moment's rest - but I don't need more than that."
"As long as it lasts, the stasis machine has no concept of time. I have no idea how long I've slept."
"All I know is it was more than enough."
"Finally, I open the hatch and emerge out into the jungle."

scene bg jungle-night
with Dissolve(2.0)

"They looked smaller from the shuttle."
"From the ground, the trees are as big and as wide as skyscrapers."
"There are leaves as big as the ship - but most of the trees don't have leaves. Instead they have porous puffs like fungi."
"The fungi rain down spores that coat the forest floor."
"I bring a GPS locator, a few meals' worth of food, and a filter for water. With all of my supplies in order, I begin climbing my way towards the signal."
"It takes twice as much effort to cover half the ground on the forest floor."
"Above me I can hear animals - birds with voices so low that the leaves shudder with the sound waves, the scuttling of what I imagine is some huge insect, the occasional ruffling of one of the giant fungi."
"Down here, though, the animals are mercifully small."
"I'm starting to relax and fall into the rhythms of the walk when something catches my eye up in the canopy."
"It's a spot of sunlight, sunlight that is otherwise blocked by the leaves and spores."
"A tree branch has been torn from a tree, leaving the spot open."
if blue1:
   "It's fresh. This must have happened recently."
if blue2:
   "The tree has started growing back. I don't know how fast anything grows here, so I don't know what that means, but it's not fresh."
if blue3:
   "I barely notice the break - a new branch has almost completely taken its place."
"It's too small to have been caused by the ark."
"My heart sinks."
"But it could still be something. I have to at least look for it."
"I squint up at the crack in the branch and follow the direction it points."
"I shimmy up a root of one of the trees and then climb up a vine until I have a good vantage point."
"Then I look out."
"The underbrush has begun to grow over it, but I can see the small crater where a ship crashed and skidded."
"At the end of the trail, I find what looks like the remains of a shuttle."
"It's been taken apart and moved - all that remains in the spot where it landed is a smallish chunk of metal that must have formed part of the energy core."
"It's hard to tell tell how big the shuttle is just from this piece, but it's definitely larger than mine."
"There's a fire pit here, too, under an outcropping of rocks. It hasn't been used in a while, from the looks of it."
"Should I go back to the shuttle? Whatever happened here, this place is abandoned now..."
"KRKRKRKRKRKRKRRKKRK"
"Instinctively I duck behind the rocks."
"That sounded like gunshots."
"I hear something rustling behind me."
"My weapon, where's my weapon? I reach for my holster, but before I can get to it I see a shadow from the trees..."
"...And a creature landing on top of it."
"The creature turns to me for a moment. It's a little dark now, so I can't see it fully..."
"But when it looks at me, its eyes glow."
"It looks at me with something I can't quite comprehend."
"Fear? Sadness? Pain? I open my mouth to say something, but it won't understand."
"Before I think to turn on my translator, it leaps back into the trees and lumbers away."
"I wait until I'm certain it's gone before stepping out from under the outcropping."
"I'm sure now... those guns were human-made. Carefully, I climb up onto the outcropping and walk towards the origin of the shots."
"I'm almost out of breath as I reach another clearing in the forest."
"The figures are dim in the dark. They're huddled together. I can't tell how many there are."
"I unholster my weapon and step towards them."
t "Hello...?"
show hector mid neutral
"At first I barely recognize them - but then it clicks."
"The freckles, the round cheeks, the big nose."
"This was the soldier who made the call over the radio."
t "Hector...? Hector Jensen?"
h "...Commander?"
"I remember he was always so awkward with me. Now, he looks like he simply doesn't have the energy for it."
"He steps towards me. His men follow suit."
"They stop just short of me. The space between us feels like a rift. They're clearly all relieved to see me, if not happy... but they're hesitant."
t "What happened to you? What happened to the ark? I was stuck on a planet. I had to reuild my ship..."
show hector mid concerned
h "Why now?"
h "We go through so much, we have to do so many terrible things, and you show up {i}now?{/i}"
"It's only now that I notice they've been crying. One soldier, standing slightly behind the others, still is."
"Behind them is a small mound of dirt."
"Come to think of it, this is the only spot with soft enough soil to dig through that I've seen since I arrived."
t "Oh. Oh, I... I'm so sorry."
show hector mid angry
h "Of fucking course you're sorry! You show up in your ship like nothing's happened. We've been dying out here, killing ourselves just to eke out a few more months."
h "Do you even have room for us? Do you even know where the ark is?"
t "...No. I don't. My shuttle only has room for me."
"The news hits the soldiers viscerally. One of them makes a sound like a sob and a groan, and another clutches his stomach as if he's going to vomit."
h "We don't even know how long it's been since the ark left. Since we landed here... since we saw our families..."
h "Arlington starved to death. Tran was so sure he could negotiate with them, and for a moment it looked like we might finally have some peace in this shithole..."
h "But now he's dead."
h "And any chance of negotiation was just scared off by your stupid ship."
h "Your ship that can only hold yourself. If you weren't so fucking selfish you might think of what happens when you land without warning, {i}Commander.{/i}"
"The venom in his words hits me harder than I expect it to."
"He thinks they're the only ones who have seen hardship out here?"
"Even his soldiers look shocked at his impropriety."
"I want to put him in his place."
"But he has been through a lot..."
menu:
   "He pauses for a moment to catch his breath. I have a chance to speak."
   "Dress him down.":
      $ speakup = True
      t "You think you're the only one with fucking problems?"
      t "The ark abandoned me! After everything I did!"
      if calypso1:
         t "After I put everything I had into the future of that ship and everyone on it, they left me alone to die!"
         t "They left my daughter without a mother!"
         t "By some miracle I had the chance to finally have some peace on that planet, but I left it behind just for the possibility of seeing them again!"
      else:
         t "After I gave everything I had to the army, when I thought they couldn't take anything else from me, they left me alone to die!"
         t "They left my daughter without a mother!"
         t "And on that planet I finally found someone who would never have left me, who really and truly cared about my well-being..."
         t "and I left it behind just for the chance of seeing them again!"
      t "But they're gone! I have no idea how long I've drifted through space searching for them by now, but they're fucking gone!"
      t "They couldn't even be bothered to leave a sign for me!"
      t "I could die before I find them!"
      t "My daughter thinks I'm dead because of them!"
      t "You have no right to talk to me about sacrifices. I have sacrificed everything. I am sacrificing everything right now."
      t "So get over yourself, pick up the pieces of your crew, and move on. Or die, I don't care. But don't lay this at my feet."
      "The soldiers fall silent. They wait for Hector to respond. I can tell from his face - he is livid. But he stops himself from showing it to his men."
      h "Stay at our camp tonight, Commander. We owe you that for your {i}suffering.{/i}"
      h "But in the morning, you leave and you never come back."
      h "We'll get over ourselves and we'll survive in this hell."
      h "But I never want to see you again."
      h "I hope for your daughter's sake that you never make it back to the ark."
      show hector mid sad
   "Apologize.":
      $ stayquiet = True
      "I swallow my pride."
      "I could tell him off now, but it would just make me look weak."
      "So instead, I lift my head and meet his eyes."
      t "I'm sorry."
      t "I didn't mean to ruin your negotiations."
      t "And I sincerely hope it wasn't my actions that caused the death of your officer."
      "The soldiers stay silent, but they look ashamed. They look to Hector for a response."
      show hector mid sad
      h "It's just that we've lost so much... I don't know how to do this. I don't know how we can move forward from here."
      "Tears well up in his eyes."
      h "We thought at least maybe you could bring us home, but..."
      h "We're stuck here, aren't we? We're stuck here. Probably for the rest of our lives."
      "I can't find the words to comfort him."
      "I don't know if there are any words that could."
      "He starts to cry. The others step forward to comfort him, and then all at once they're crying together."
      "I stand away from them. All I can do is watch with the solemnity to which I became accustomed on the ark."
      "It surprises me how much that solemnity hurts right now."
      "After what seems like a long time, they quiet down."
      "They look defeated... but relieved."
      h "...We should get back to the camp."
label after_speakup:
"We walk in silence back to the camp."
"The soldiers are trying to keep their distance from me, so I walk a little behind them."
if speakup:
    "I feel like I should feel bad for what's happened, but I don't."
    "In fact, I feel relieved."
    "They are where they need to be. They're determined to survive. They know this is their life now."
    "And I know that I'm better off without them."
if stayquiet:
    "The fight is over - and it ended well."
    "So why is it that I feel sadder and more alone than when I got here?"
    "Why is it that I want to get off of this planet as soon as possible?"
    "No matter the reason, I resolve to leave tomorrow morning."
    "It's clear I'm not welcome here."
"We reach the camp."
"The soldiers walk past the energy core along the shuttle's trail. Hector pulls back a blanket of underbrush that I hadn't noticed."
"Behind it is a door made from the shuttle's hull."
"Another soldier opens it, and they beckon me in."
"Inside, it's cramped, but cozy. Luminescent plants and mushrooms line the walls."
"They seem to have planted them. They keep the cave dimly and warmly lit."
h "You can sleep in Tran's spot."
t "Thank you."
"I avert my eyes from him and lie down on top of his sleeping bag."
"It doesn't seem right to sleep inside of it, even though it's a cold night."

scene bg black
with Dissolve(2.0)

"The cold keeps me awake as the others quietly curl up into their bags."
"I don't think I'm the only person awake, though. It's too quiet."
"I sit up on my elbows and scan the room, and I find Hector looking up at me."
"For a moment, we just look at each other."
"I remember how awkward he used to be..."
"I turn away and lie back down on my other side."
"I manage to sleep a little, if lightly and uncomfortably."

scene bg jungle-night
with Dissolve(2.0)

"It's hardly light out, and the other soldiers are still asleep, but it's time for me to go."
"I zip up my bag and slip out through a crack in the door."

show hector mid concerned

"Hector is outside, waiting for me."
h "You have everything?"
t "Yeah."
"The silence between us is heavy."
t "...Good luck with them."
h "Thank you."

if speakup:
   hide hector mid concerned
   "I turn on my heel and leave, climbing up a tree root up and over the hill towards my shuttle."
   "As I'm about to descend, I hear a rustling in the trees above me."
   "I take cover behind the branch and look back at the clearing."
   "The creatures land in front of Hector. He looks surprised and concerned. He doesn't have a weapon."
   "But the creatures don't attack. They're holding something in their hands."
   "They're distracted with him, and this is none of my business. I won't get caught up in it."
   "I turn and make my way down the hill as quietly as I can. When I get to the bottom, I break into a run."
   "I listen for rustling behind me, but I don't hear anything. I'm safe."
   "I make it to my ship, run the engines and fly up into the sky as quickly as I can."
   "The planet feels good behind me, and by the time I get back to space, I feel like a weight has been lifted from my shoulders."

if stayquiet:
   "I am about to turn to leave when I hear a rustling in the trees above us."
   "I reach for my weapon, but Hector stops me."
   h "No. Not now."
   "I decide to trust him. For now."
   show friend dark
   "The creatures land in front of us. They barely make a sound."
   "They are at least eight feet tall. They look like spiders, but they move more like monkeys, or maybe cats - with a grace and steadiness that makes them all the more intimidating."
   "One of them stares at me."
   "I remember it from before. I understand its expression now - the expression that felt so indecipherable before."
   "It's remorseful."
   "It steps forward and shifts its eyes from me to Hector. It has something in its hands."
   "It's a jacket - Tran's jacket."
   "The creature makes a low, guttural noise, something like a growl or a purr. The sound is layered, with clicks and harmonics I can't quite describe."
   "My universal translator flickers to life in my ear."
   u "Part of me is dead... with your friend."
   u "This is what remains."
   "I turn to Hector to make a translation, but he is already accepting the jacket."
   "He can't know exactly what they're saying, but there is recognition in his eyes."
   show hector mid neutral
   "He nods to me solemnly, a signal that I can leave."
   "I give the creatures one last look and turn away from them."
   hide hector mid concerned
   hide friend dark
   "I climb up the root and over the hill, and without looking back make it back to my ship."
   "The hatch closes behind me."
   "I sit in the ship for a long, quiet moment."
   "Then, as I bring the energy core to life, I find myself letting out a furious, growling scream."
   "I let myself feel it until I get to space."
   "It's alright now. I'm alone again."
   "I'm always alone."
   "I sit back in my chair and breathe."

scene bg space
with Dissolve(2.0)

jump space3

label space3:

"The ship's navigation systems come back to life with a hum."
"There's only one planet to choose now."

if blue1:
   if green2:
     jump orange3
   else:
     jump green3
elif green1:
   if orange2:
     jump blue3
   else:
     jump orange3
else:
   if blue2:
     jump green3
   else:
     jump blue3

label green3:

$ revolted = False
$ understand = False
$ burial = False
$ leavebe = False

"I type in the coordinates for the green planet."
"It looks like it would harbor the most similar climate to Earth, given the distance to its sun..."
"I'll take that small hope. It's better than nothing."
"The ship lurches forward, and then the stars are a blur all around me."
"I watch them go by for a while. I look at the screens one by one. I examine the control panels, trace out the alien lettering on my chair, and poke at the innoculation machine."
"I do anything to avoid stasis for just a few more minutes."
"But then my mind wanders to Penelope."
"What is she thinking right now? Does she miss me?"
"What does she think about when she thinks about me?"
"My stomach ties itself in knots."
"I recline my chair and press my arms into the armrests."
"I let the needles prick me and imagine myself staring up at the sky from solid ground, on a planet with fresh air and clean water where I can make a home."
"Is that planet Earth? Is it Calypso? Or is it a place I'll never find?"
"The thought haunts me as I drift away."

scene bg black
with Dissolve(2.0)

"My shuttle pulls into the ark."
"I open the hatch and I'm in our room again."
"Penelope is waiting for me."
p "I've missed you, mom."
p "So much."
p "The ark's missed you too."
p "They know what you did."

if speakup:
   p "They know you hate your men."
   p "They know you hate all of us."
   p "You've always hated us."
   "She is holding a hammer."
   "She swings it and it hits the window."
   "The glass breaks into a spider's web of cracks."
   "She hands the hammer to me."
   p "They want you to take the final swing."
   p "You've always wanted this, right?"
   p "Go on."
   p "You're so worried about time... so end it."
   p "End it, now."
   p "{i}End it!{/i}"

if stayquiet:
   p "They know your secrets."
   p "They know how much you resent us."
   p "They know you wish you weren't with us."
   "She is holding a gun."
   "She loads it, turns the safety off, and hands it to me."
   p "They want you to do it yourself."
   p "They know this is what you wanted."
   p "They wanted me to watch, so I know too."
   p "So do it, mom."
   p "You're so sick of everyone on this ark... so end it."
   p "End it, now."
   p "{i}End it!{/i}"

if detonate:
   p "They know what you are."
   p "They know what you would do to us if we became inconvenient."
   p "You want us to think you make sacrifices..."
   p "You want us to think that we're important to you..."
   p "But how important are we, really?"
   "She is holding a bomb."
   p "This is how important we are."
   p "They wanted you to show them."
   p "They wanted you to show me."
   p "So show me."
   p "Show me how much you care."
   p "Show me what you would do if we stopped believing in you."
   p "Show me."
   p "{i}Show me!{/i}"

if killscout:
   p "They know what you think of them."
   p "They know what you think of yourself."
   p "You call it heroism. You call it sacrifice..."
   p "But the truth is, their opinions mean nothing to you."
   p "You only care about yourself."
   p "You only trust yourself."
   "She is holding a switch... it's the switch that opens the hangar doors."
   p "Get out."
   "She pushes me from our room and into the hangar."
   p "Get out!"
   "She pulls the switch. The air drains from my lungs."
   "Everything spins around me."
   p "{i}Get out!{/i}"

if inform:
   p "They know how you are."
   p "They know you'd betray anyone... even a child."
   p "Even me."
   p "As soon as we become a problem, you abandon us."
   "She is holding a knife."
   "She is the boy now, and I am his sister."
   "I look down and I am bleeding and rotting and I am made of ash."
   p "This is what you deserve."
   p "Die, mother."
   p "Die."
   p "{i}Die!{/i}"

if keepsecret:
   p "They know what you'd do for me."
   p "They know that you wouldn't stop me."
   p "Even if I killed everyone on this ark..."
   p "You wouldn't stop me."
   p "You'd be proud of me."
   "She is the boy now, and I am his father."
   "She is holding a knife, and we are covered in black."
   p "Come on, mom. Take the first hit."
   "Penelope's body lies in front of me."
   "Penelope hands me her knife."
   p "Take the hit."
   p "Do it..."
   p "Kill her!"
   p "{i}Kill her!{/i}"

scene bg space
with Dissolve(2.0)

"I wake up a little at a time, and then all at once. I gasp sharply and open my eyes with a start."
"I feel as if I've almost drowned, but my body isn't starved for air."
"Suddenly full of a jittery, fearful energy, I pull my chair forward."
"The planet is dead ahead."
"When I first look at it, I have to convince myself that I haven't returned to Earth."
"Its continents are larger, yes, and they're different shapes - but the bright greens and calm blues, cut across by languid clouds..."
"It's like home."
"As we pull in, there is one distinct difference:"
"This planet has scars."
"Some of them are from mining, but from the looks of it, vast tracts of this land were once covered in cities and factories."
"But the cities are dark."
"Even from up here it's clear they've been long abandoned."
"I turn back to my screens. They're reading no beacons or signals from the ark..."
"But I'm low on food, and my energy core's readings are fluctuating dangerously."
"It needs a rest. So I have to land."
"I pick a spot that looks as clear as possible of the cities and structures that litter the planet's surface."
"The ship makes a smooth landing just near what looks like a forest."

scene bg field-day
with Dissolve(2.0)

"When I emerge from the shuttle, I realize that this field is far from clear:"
"I've landed at the edge of a huge city of tents."
"The grass-green fabric must have disguised their appearance from the sky."
"I climb back into the shuttle and try to turn it on. I don't want any trouble."
"But it's already gone to sleep. It will need to charge for at least a few hours before I can get it back in the air."
"Resigned, I open the hatch again - only to find I'm surrounded by at least a hundred aliens."
"They're a little taller than me on average. Their legs bend backwards like an ostrich."
"They all look built for running, but other than that they're remarkably diverse:"
"I see groups with long arms, shorter and stockier groups, others who are tall and thin."
"None of them look outright hostile, but they don't look surprised, either."
"They're speaking in hushed hisses and clicks. From this distance, my translator doesn't recognize the sounds."
"Finally, the circle parts at one end and an individual steps forward, taller and much older than the rest. This must be their leader."
show leader happy
l "Welcome to our land, traveller."
l "We hope you've come here safely and peacefully."
"This is a warmer welcome than I anticipated."
"And they seem utterly uninterested in either my translator or my shuttle."
t "I have."
show leader neutral
l "Tell us, where are you from? What brings you here?"
t "I was separated from my people. I'm looking for them."
t "They were on a bigger ship. They might have passed through here. Have you seen them?"
l "We haven't."
show leader sad
l "And for you... I am so sorry."
"The others repeat the words."
t "Thank you."
l "We can't offer much - we're still settling here - but we have a warm meal and a bed for you, if you'll take it."
"I frown at them, still unsure if this is real."
t "Are you sure?"
show leader happy
l "We take pride in our hospitality for the travellers who pass through our planet."
"The leader beckons me to join them, so I make sure my shuttle is secure and then happily oblige them."
"I have to stop myself from staring at the patchwork of interlocking tents that makes up this town."
"The smaller ones are residential, the leader explains to me; the larger ones are public buildings. We walk past an infirmary, a dining hall and a tent for children."
show leader neutral
"As we pass the dining hall, the leader gets some food for us: two bowls of hot stew, filled with meat, root vegetables and a pearl-shaped grain."
"Then, food in hand, we walk to the center of the town."
"We come to an area clear of tents, and immediately I see why: it's a giant crater."
"Grass has started to grow over the impact, but at the time it must have been devastating."
"At the epicenter stands a monument made of wood and what looks like found pieces of metal. More of this metal sits at the bottom of it."
"The monument depicts one of their kind, standing tall and watchful over the tents."
"Its expression is solemn, almost melancholy."
"The bottom half of the structure is covered in what looks like writing, but of course I can't read it."
"The leader sits down on the grass at the edge of it, and I join him."
t "What does it say?"
l "It's a dedication: to the great and terrible violence that has taken the weights from our legs."
if calypso1:
   "There's something almost compelling about the words, but when I try to think about them, I can't get past how sick they make me feel."
else:
   "I should think of it as too morbid, but I find it strikes a chord."
t "What happened?"
l "We used to be nomadic. We combed the land for the remains of technology from the others who came before us here."
l "Our jobs within the flock were arranged for us based on our biology. It's why our bodies are so different, we thought - some of us were just built for certain things."
l "It was a good life for some, but for others it was rigid. For many it was oppressive."
l "Some of us wanted to settle down."
show leader sad
l "There was a war."
l "It lasted a long time... but that scout ended it."
t "With a {i}bomb?{/i}"
l "By that time, their flock was the last holdout. Their own social structure was eroding. There was widespread famine in the flock, but none could leave."
l "Or so we're told. We don't have many details. Those who joined us don't talk about it very often."
l "That scout brought a swift end to it. After the explosion, the flock collapsed. Their leader died."
l "Now that we're at peace, some of ours wanted to commemorate them."
t "What happened to the scout?"
l "They died in the explosion."
t "But why did they do it in the first place?"
t "What drove them to that point?"
l "We'll likely never know."
"I put down my food and walk down to the statue."
"Its face is lithe and pointed, almost aerodynamic."
"But its expression, at least to me, is indiscernable."
if goodspeech:
   "I think of the things I've done to make things better for others."
   "But I don't think of those things as violence."
   "Should I? The thought disturbs me."
if badspeech:
   "I think of the things I've done to make things better for others."
   "Those great and terrible acts of violence..."
   "I wonder if those I've met feel lighter for them."

if speakup:
   "I think of everything that I've sacrificed, and of how little people have noticed."
if stayquiet:
   "I think of all the violence I've done to myself to make things better for others."
   "Even now, the weight is still so heavy."
"I return to the leader."
l "What's on your mind?"
menu:
   t "I think I can relate to that scout."
   "They were selfless.":
      $ selfless = True
      t "I've made sacrifices for my people too."
      t "I like to think that my people understand why I did what I did..."
      t "But I'm not sure they do."
      if goodspeech:
           t "It's easier for them to glamorize what I did, but in truth, it wouldn't have been a sacrifice if it was glamorous."
      if badspeech:
           t "It's easier for them to think that on some level, I'm happy with the choice I made."
           t "But it wouldn't have been a sacrifice if that were true."
      if speakup:
           t "They think I was some lofty hero with noble goals."
           t "They think of my sacrifices as glamorous."
           t "But the truth is, I would have been so much happier if I'd forgotten about all of them."
      if stayquiet:
           t "They see what I've done and they see something beautiful."
           t "They don't see what pain I've put myself through for their sakes."
      t "That's what it is to be selfless: to do great violence to yourself so that others might find their burdens lessened."
      t "And to make that violence invisible so they never know about it."
      t "I wonder..."
      t "What violence did that scout do to himself to make this place what it is?"
   "They were desperate.":
      $ desperate = True
      t "I assume they were working alone?"
      l "Yes, they were."
      if childhome:
         t "The pain of enduring a system that is actively hostile towards you..."
      if newhome:
         t "The pain of hoping for a better future, only to watch that future slip away as things got worse and worse..."
      if keepsecret:
         t "The pain of uncertainty - of watching things get worse and not knowing how to stop it..."
      if inform:
         t "The pain of divided loyalties - of wanting to stay with their flock but being unable to stand the atrocities they were committing..."
      t "To be alone with all that pain must have been unbearable."
      t "If only they knew that their pain had a purpose."
l "You're right..."
l "Sometimes I wish that I could go back in time and tell them all that their pain has accomplished."
if calypso1:
   t "Yeah, maybe it would be nice to know."
   t "Even if it didn't change their situation, it would be something to look forward to."
else:
   t "I'm not sure it would change anything..."
   t "And if it did, maybe they wouldn't have ended up accomplishing it in the first place."
"We finish our food in silence."

scene bg field-night
with Dissolve(2.0)

"The leader has me sleep in a communal tent with a few others."
"We make small talk and swap folk tales by the fire. When I see that they're trying to start a garden - and failing badly - I show them how I used to tend to mine."
"The grass is soft and pillowy. I sleep as if I'm in a luxury bed."
"Before I leave the next day, I wake up early and go to the monument again."
"I wonder if there's a monument to me out there somewhere... and what's written on the bottom of it."
if selfless:
    t "I understand what you've done..."
    t "Even if they don't."
    t "I just thought you should know that someone does."
if desperate:
    t "I'm sorry for what you had to go through."
    t "And I'm sorry you had to do it alone."
    t "We heroes should stick together, when we can."
"I touch the letters on the monument once more, and climb back up the crater."
"The flock sends me off with well-wishes and kind thoughts, but when I climb into my seat, I look back to find them holding each other."
"Are they mourning?"
"Are they mourning for me?"
"I want to watch them for longer. I want to get back out and ask them what they're doing."
"But before I can, the shuttle whirrs to life and floats into the air."
"I watch the tents disappear back into the fields, and settle back into my seat as the fields fade into the white of the clouds."

scene bg space
with Dissolve(2.0)

"Space feels a little less empty..."
if selfless:
    "And the weight on my shoulders feels a little lighter."
if desperate:
    "And I feel a little less alone."

jump space4

label orange3:

$ understand = False
$ revolted = False
$ desperate = False
$ lonely = False

"I punch in the coordinates for the orange planet."
"A warmer planet might be more promising for settlement..."
"It's a slim chance, but I'll have to take it."
"I engage the ship's engines and watch the stars turn to blurry lines out the window."
"Penelope always preferred the cold."
"She was a weird kid like that."
"I suppose she never got to do anything fun in the heat, so for her it was just uncomfortable."
"She never got to go to the beach on a hot summer's day, or take a nap in the warmth of the sun..."
"If she had, would she still prefer the cold?"
"Or is she sitting on that planet right now, feeling uncomfortable and grumpy that of all the planets in the galaxy, they had to pick the hot one?"
"I wouldn't have let them pick the hot one, I think as I recline the chair and slip my arms into the armrests."
"Even if we had to go it alone, I would have made sure we built our home somewhere she liked."
"The thought lingers with me as I drift into stasis."

scene bg black
with Dissolve(2.0)

"My shuttle pulls into the ark."
"I open the hatch and I'm in our room again."
"Penelope is waiting for me."
p "I've missed you, mom."
p "So much."
p "The ark's missed you too."
p "They know what you did."

if speakup:
   p "They know you hate your men."
   p "They know you hate all of us."
   p "You've always hated us."
   "She is holding a hammer."
   "She swings it and it hits the window."
   "The glass breaks into a spider's web of cracks."
   "She hands the hammer to me."
   p "They want you to take the final swing."
   p "You've always wanted this, right?"
   p "Go on."
   p "You're so worried about time... so end it."
   p "End it, now."
   p "{i}End it!{/i}"

if stayquiet:
   p "They know your secrets."
   p "They know how much you resent us."
   p "They know you wish you weren't with us."
   "She is holding a gun."
   "She loads it, turns the safety off, and hands it to me."
   p "They want you to do it yourself."
   p "They know this is what you wanted."
   p "They wanted me to watch, so I know too."
   p "So do it, mom."
   p "You're so sick of everyone on this ark... so end it."
   p "End it, now."
   p "{i}End it!{/i}"

if detonate:
   p "They know what you are."
   p "They know what you would do to us if we became inconvenient."
   p "You want us to think you make sacrifices..."
   p "You want us to think that we're important to you..."
   p "But how important are we, really?"
   "She is holding a bomb."
   p "This is how important we are."
   p "They wanted you to show them."
   p "They wanted you to show me."
   p "So show me."
   p "Show me how much you care."
   p "Show me what you would do if we stopped believing in you."
   p "Show me."
   p "{i}Show me!{/i}"

if killscout:
   p "They know what you think of them."
   p "They know what you think of yourself."
   p "You call it heroism. You call it sacrifice..."
   p "But the truth is, their opinions mean nothing to you."
   p "You only care about yourself."
   p "You only trust yourself."
   "She is holding a switch... it's the switch that opens the hangar doors."
   p "Get out."
   "She pushes me from our room and into the hangar."
   p "Get out!"
   "She pulls the switch. The air drains from my lungs."
   "Everything spins around me."
   p "{i}Get out!{/i}"

if inform:
   p "They know how you are."
   p "They know you'd betray anyone... even a child."
   p "Even me."
   p "As soon as we become a problem, you abandon us."
   "She is holding a knife."
   "She is the boy now, and I am his sister."
   "I look down and I am bleeding and rotting and I am made of ash."
   p "This is what you deserve."
   p "Die, mother."
   p "Die."
   p "{i}Die!{/i}"

if keepsecret:
   p "They know what you'd do for me."
   p "They know that you wouldn't stop me."
   p "Even if I killed everyone on this ark..."
   p "You wouldn't stop me."
   p "You'd be proud of me."
   "She is the boy now, and I am his father."
   "She is holding a knife, and we are covered in black."
   p "Come on, mom. Take the first hit."
   "Penelope's body lies in front of me."
   "Penelope hands me her knife."
   p "Take the hit."
   p "Do it..."
   p "Kill her!"
   p "{i}Kill her!{/i}"

scene bg space
with Dissolve(2.0)

"I wake up to a red glow."
"Is it sunlight?"
"How long was I napping for? Is it sundown already?"
"I open my mouth to call to my grandma."
"Please tell me I didn't oversleep again..."
"But I didn't oversleep. The stasis pod always wakes me up ontime."
"No, the red glow is from the planet, hovering above me."
"It's almost entirely orange and red - deserts lined with oxidized iron, from the looks of it."
"Lines of green and blue slice and swirl across it. So it must have some fresh water. I wouldn't be surprised if there was more underground."
"There's no clear signs of the ark, but the ship is reading intense bursts of energy from underground."
"If they're here, they might have chosen to live underground - perhaps to access water, or to stay safe from the sun."
"In any case, I need to land to recharge the energy core. And I should eat something."
"I locate the region with the strongest signatures: a mountainous area near the planet's north pole."
"I put in the coordinates and carefully steer the ship towards the atmosphere."
"The oranges and reds become even more brilliant as I descend. The mountains look like marble - they're almost psychedelic."
"There's a small strip of flat land ahead. I slow the ship, bring it about, and make my landing."

scene bg mountains
with Dissolve(2.0)

"I push open the hatch and climb out, once I'm sure I'm fully innoculated."
"The sun beats down on me. I can feel myself sweating already. The air smells metallic and faintly of mud."
"I'd want to live underground too, if I landed here."
"I decide to find some shade before anything else."
"The sun is already disorienting me, making me dizzy and dehydrated... this could be bad."
"But there are no trees to be found."
"I wander a ways away from the shuttle, looking for a valley or a river or something -"
"But there's nothing. Just more mountains."
"I squint and try to see something, anything through the piercing sunlight."
"What I see are holes."
"They look tiny in the distance, but as I examine the hills nearby I can see larger ones."
"Now that I see them up close, they don't look like holes anymore."
"They're burrows."
"The thought of fresh water and shade emboldens me, and I frantically search for the nearest one."
"I see one just a few feet away on the next hill. I run for it."
"These burrows are huge. This one must be at least six feet in diameter!"
"I step forward towards it. I bet it leads to an underground river..."
"Maybe Penelope's there. Splashing around, playing in the water. Learning to enjoy warm weather for once."
"I hear splashing inside, too."
"I climb down inside the burrow and follow the sound."

scene bg cave
with Dissolve(2.0)

"The splashing stops."
t "Penelope?"
"I get to the water source. It's a tiny underground lake. Light from outside reflects off of the surface and paints patterns on the ceiling."
"Faintly, I can see objects in the deeper caves. Furniture?"
"The floors are stained with strips of black - some unfamiliar chemical, perhaps, though I see no residue of it on the ceiling."
"But I don't have time for that--"
"There's something in the water."
"It looks up at me. It's a little like a lizard, but with long legs and fangs like a wolf."
"It's got some sort of meat in its mouth."
"It snarls at me, drops the meat, and lunges."
"I leap back, grab my gun and fire."
"The first shot hits its leg, but it hardly notices."
"The second shot hits it in the head."
"It falls to the ground."
"I take a long breath. I guess I just found dinner."
"I step into the water to look at what the beast was eating, and find a tiny body floating there."
"It looks a little like an ant, but about as large as a human child."
"The beast didn't kill it, that much is clear - it looks gaunt and thin. I think it starved to death."
"Its face looks vulnerable - it has big, expressive eyes."
"Gingerly, I lift it from the water and lay it on the ground."
"I'm about to leave when I see another body, hidden from view in the darkness of the cave."
"It looks like the same species, but this one is an adult, almost as tall as me."
"Unlike its child, it looks like it died violently."
"Was this the lizard's work?"
"It could be... but the wounds on this one's body are precise."
"It looks like it was stabbed in the stomach - probably with a weapon, not a tooth."
"I recoil when I see the black liquid in a puddle around its body. It's blood."
"So that was blood at the entrance as well..."
"It was dragged here."
"All of a sudden I feel sick to my stomach."
"I look around the cave. Now that my eyes have adjusted, I can see the outline of the home this place once was."
"At the far end of the lake, there's a dining table. Off to the side there are two small sleeping areas."
"There's a desk. Arranged on top of it in a little pattern are tiny rocks and gems of all colours and shapes."
"I notice what looks like a book. The paper feels coarse like sand. It's filled with drawings done in thick black charcoal lines."
if goodspeech:
   "I flip through to a picture of a family."
   "They're splashing in playing in the water together: a parent and two children."
   "Their eyes have a haunting quality to them - they're just a little too wide, looking more at me than they are at each other."
if badspeech:
   "I flip to a picture of the cave from outside."
   "The cave looks peaceful and calm in the center of the frame, but encroaching in from the edges are the spindly branches and arms of shrubs."
if simplicity:
   "I flip to a picture of one of the aliens from close up. It looks younger than the body I found - it's smaller and rounder, and its eyes are big and hopeful."
   "But it doesn't look happy. Its eyes are hard to read, but to me it looks like pain, or perhaps fear."
if danger:
   "I flip to a close-up picture of the adult alien. It's drawn looking down at the viewer."
   "I'm not sure whether to read contempt or care into its face. Perhaps both."
if speakup:
   "Next, I turn to a picture drawn from farther away, looking down on the cave."
   "The mountains in the distance and the sky are bright, but the cave itself is drawn with thick, dark strokes."
   "It looks foreboding, like a warning: stay away."
if stayquiet:
   "Next, I turn to a picture drawn from farther away, looking down on the cave."
   "The mountains in the distance and the sky are bright, but the cave itself is drawn with thick, dark strokes."
   "It looks like a trap. Someone's trapped there and they can't get out."
if detonate:
   "Next, I turn to a picture of one of the aliens. It's from afar, but the alien takes up almost the entire page."
   "It's larger than the others - they bow and kneel before it, bearing gifts for it."
   "In its eyes I see anger and violence: a tyrant ruling over its subjects."
if killscout:
   "Next, I turn to a picture of one of the aliens. It's from afar, but the alien takes up almost the entire page."
   "It's larger than the others - they bow and kneel before it, bearing gifts for it."
   "In its eyes I see cold, quiet pride: the face of someone who's done terrible things to get where they are."
"Finally, I turn to a portrait."
"It's the spitting image of the dead child, staring straight ahead at me with a life the other pictures don't have."
if calypso1:
   "It looks tentative and fearful, but hopeful too."
else:
   "It looks tired. Weighed down by the world. And it looks so afraid."
if truth:
   "I feel like it's Penelope staring back at me, surviving all alone out there, waiting for me to find her."
else:
   "I feel like it's Penelope staring back at me, terrified and alone and confused, wondering where I am."
"I put the book down."
"Just next to the book is what looks like a pantry. Luckily, it's filled with canned foods."
"I open one and eat it. It has the texture of porridge, but tastes more like dragonfruit."
"My stomach seems to tolerate it, at least."
"It will have to do for a meal. I eat another can."
"When I'm finished eating, all that's left are the bodies."
"I've intruded into their home, eaten their food."
menu:
   "I should..."
   "Bury them.":
      $ burial = True
      $ leavebe = False
      "I find what looks like a scoop for water and dig two holes side by side near the mouth of the cave."
      "I dig until I hit the stone."
      "Hoping it's deep enough to ward off scavengers, I lay the bodies carefully next to each other and cover them with dirt."
      "I find a couple of large stones and place them over the graves."
      "I feel like I should say something."
      if calypso1:
         t "I hope you find your way, wherever you've gone."
      else:
         t "I hope you find the peace you didn't find here."
      jump after_burial
   "Leave them be.":
      $ burial = False
      $ leavebe = True
      "I've intruded enough. And I have no idea what this species does with their dead."
      "All I know is this family. This looks tragic to me, but for all I know it could be normal in their world."
      "I resign myself to the complete otherness of the situation."
      "I lay the bodies next to each other in the sleeping area."
      if calypso1:
         t "I hope they find their way."
      else:
         t "I hope they find some peace."
      jump after_burial
label after_burial:

scene bg black
with Dissolve(2.0)

"By the time I emerge from the cave, it's dark, but I manage to make my way to the shuttle."
"I'm relieved to find the shuttle's energy core is charged. I want nothing more than to leave this planet right now."

scene bg space
with Dissolve(2.0)

"I find myself still shaken by the scene, even when the planet is far behind me."
"Is that what I'll find, when I find Penelope?"
"Did she starve to death waiting for me to come back?"
"I find myself almost in tears at the thought."
"I have to put it out of my mind, though... so I push it to the back of my thoughts and turn to the screens."

jump space4

label blue3:

$ burial = False
$ leavebe = False
$ desperate = False
$ lonely = False

"I put in the coordinates for the blue planet."
"The higher temperature variation could mean a higher likelihood for inhabitability."
"...That's what I tell myself, but it feels like I'm reassuring myself more than anything."
"The ship's propulsion systems come to life, and soon I'm accelerating through space watching the stars go by above me."
"Penelope's game broke too."
"I let myself think of her for a moment, but it hurts too much."
"At least if I'm asleep it'll hurt less."
"I'm still not sure how long I'll be asleep, but I put that thought out of my mind and recline my chair backwards."
"I settle my arms into the armrests and feel the needles prick my wrists."
"At the edge of sleep, I still feel like I'm in the water with Calypso."
"I swear I can feel it lapping against my hair."

scene bg black
with Dissolve(2.0)

"My shuttle pulls into the ark."
"I open the hatch and I'm in our room again."
"Penelope is waiting for me."
p "I've missed you, mom."
p "So much."
p "The ark's missed you too."
p "They know what you did."

if speakup:
   p "They know you hate your men."
   p "They know you hate all of us."
   p "You've always hated us."
   "She is holding a hammer."
   "She swings it and it hits the window."
   "The glass breaks into a spider's web of cracks."
   "She hands the hammer to me."
   p "They want you to take the final swing."
   p "You've always wanted this, right?"
   p "Go on."
   p "You're so worried about time... so end it."
   p "End it, now."
   p "{i}End it!{/i}"

if stayquiet:
   p "They know your secrets."
   p "They know how much you resent us."
   p "They know you wish you weren't with us."
   "She is holding a gun."
   "She loads it, turns the safety off, and hands it to me."
   p "They want you to do it yourself."
   p "They know this is what you wanted."
   p "They wanted me to watch, so I know too."
   p "So do it, mom."
   p "You're so sick of everyone on this ark... so end it."
   p "End it, now."
   p "{i}End it!{/i}"

if detonate:
   p "They know what you are."
   p "They know what you would do to us if we became inconvenient."
   p "You want us to think you make sacrifices..."
   p "You want us to think that we're important to you..."
   p "But how important are we, really?"
   "She is holding a bomb."
   p "This is how important we are."
   p "They wanted you to show them."
   p "They wanted you to show me."
   p "So show me."
   p "Show me how much you care."
   p "Show me what you would do if we stopped believing in you."
   p "Show me."
   p "{i}Show me!{/i}"

if killscout:
   p "They know what you think of them."
   p "They know what you think of yourself."
   p "You call it heroism. You call it sacrifice..."
   p "But the truth is, their opinions mean nothing to you."
   p "You only care about yourself."
   p "You only trust yourself."
   "She is holding a switch... it's the switch that opens the hangar doors."
   p "Get out."
   "She pushes me from our room and into the hangar."
   p "Get out!"
   "She pulls the switch. The air drains from my lungs."
   "Everything spins around me."
   p "{i}Get out!{/i}"

if inform:
   p "They know how you are."
   p "They know you'd betray anyone... even a child."
   p "Even me."
   p "As soon as we become a problem, you abandon us."
   "She is holding a knife."
   "She is the boy now, and I am his sister."
   "I look down and I am bleeding and rotting and I am made of ash."
   p "This is what you deserve."
   p "Die, mother."
   p "Die."
   p "{i}Die!{/i}"

if keepsecret:
   p "They know what you'd do for me."
   p "They know that you wouldn't stop me."
   p "Even if I killed everyone on this ark..."
   p "You wouldn't stop me."
   p "You'd be proud of me."
   "She is the boy now, and I am his father."
   "She is holding a knife, and we are covered in black."
   p "Come on, mom. Take the first hit."
   "Penelope's body lies in front of me."
   "Penelope hands me her knife."
   p "Take the hit."
   p "Do it..."
   p "Kill her!"
   p "{i}Kill her!{/i}"

scene bg space
with Dissolve(2.0)

"I feel a terrible weight on my chest."
"The weight wakes me up, but my body refuses to move."
"I try to open my eyes but my lids are so heavy... I can barely keep them open."
"I lie like this for a while. I'm not sure how long."
"The stasis is coming offline."
"My body starts to feel lighter."
"Finally I can move."
"I open my eyes to find that we're about to begin our descent."
"Above me floats the planet."
"The dot on my map was blue, but the surface of the planet is a blend of pinks and yellows, with deep green oceans and massive storms."
"Entire swaths of it are desert yellow, and the poles are dotted with white."
"Calypso was right about the temperature variation."
"I'm distracted from the view by a faint beeping from one of the screens."
"I pull the chair back upwards and examine it."
"The beeping is a beacon from the planet's surface -"
"One of our distress beacons."
"The ark could have landed here. Penelope could have--"
"The ship shudders as we start to hit the planet's upper atmosphere. I turn my attention to the control panel."
"I angle the ship above the planet and punch in the coordinates of the beacon."
"The ship shudders as we hit the lower atmosphere, but it stays steady."
"I look down at the ground. It is a flood of colours: pinks, yellows and greens."
"It looks like a jungle."
"Safer than the desert, I think - but then I realize how low we are to the ground."
"The trees are huge."
"I take control of the ship and decelerate."
"Then, carefully, my eyes fixed on the ship's screens, I lower it into the forest."
"I manage to dodge the tree branches and find a soft landing spot on the forest floor."

scene bg black
with Dissolve(2.0)

"Before I leave the ship, I innoculate myself and eat some preserved foods Calypso left for me."
"I give myself a moment's rest - but I don't need more than that."
"As long as it lasts, the stasis machine has no concept of time. I have no idea how long I've slept."
"All I know is it was more than enough."
"Finally, I open the hatch and emerge out into the jungle."

scene bg jungle-day
with Dissolve(2.0)

"They looked smaller from the shuttle."
"From the ground, the trees are as big and as wide as skyscrapers."
"There are leaves as big as the ship - but most of the trees don't have leaves. Instead they have porous puffs like fungi."
"The fungi rain down spores that coat the forest floor."
"I bring a GPS locator, a few meals' worth of food, and a filter for water. With all of my supplies in order, I begin climbing my way towards the signal."
"It takes twice as much effort to cover half the ground on the forest floor."
"Above me I can hear animals - birds with voices so low that the leaves shudder with the sound waves, the scuttling of what I imagine is some huge insect, the occasional ruffling of one of the giant fungi."
"Down here, though, the animals are mercifully small."
"I'm starting to relax and fall into the rhythms of the walk when something catches my eye up in the canopy."
"It's a spot of sunlight, sunlight that is otherwise blocked by the leaves and spores."
"A tree branch has been torn from a tree, leaving the spot open."
if blue1:
   "It's fresh. This must have happened recently."
if blue2:
   "The tree has started growing back. I don't know how fast anything grows here, so I don't know what that means, but it's not fresh."
if blue3:
   "I barely notice the break - a new branch has almost completely taken its place."
"It's too small to have been caused by the ark."
"My heart sinks."
"But it could still be something. I have to at least look for it."
"I squint up at the crack in the branch and follow the direction it points."
"I shimmy up a root of one of the trees and then climb up a vine until I have a good vantage point."
"Then I look out."
"Once, this clearing was a crater - I can see the skid marks from where it landed and came to a stop."
"Now, it's a garden."
"One side of the hull of the shuttle has been bent into a mechanism that carries water to the plants from an outcropping of rocks."
"What used to be the energy core is now a makeshift pot - tiny flowers peek out from the holes at its sides."
"Built out of the rocks and crags are three small hutches."
"Off to the side is a fire pit surrounded by stones fashioned into benches."
"Spores from the trees rain down on the scene, coating the edges of the site in fluff."
"It's almost idyllic."
"I make a bit of noise as I climb down carefully from my perch up the hill."
"I make a little too much noise. Above me, a tree branch rustles - and when I look down there is a massive creature staring at me."

show friend light

"It looks like a huge spider - at least seven feet tall with its limbs, if I were to guess - but it moves like a cat or a monkey, with a sort of steady, acrobatic grace."
"Its eyes are faintly luminescent. They're searching me - it doesn't look hostile yet, but it is confused and nervous."
"It makes a low, guttural purr - but the sound is melodic, layered and complex."
"My universal translator clicks to life."
u "Did you come from the sky-house?"
"...It must be glitching."
t "I'm sorry? I--"
h "It's alright! We know her. She was a friend."
show hector old surprised behind friend
"A man emerges from the hut at the side of this creature."
"A man! A human man!"
"At first I'm so startled to see one of my own that I don't recognize him, but then it clicks--"
"The freckles, round cheeks, big nose. I know this man."
"He was the one who made the radio signal on Calypso."
t "Hector...?"
h "Commander! It's been so long."
show hector old happy
"Hector steps forward and pulls me into a hug."
"I return the gesture as best I can."
"But my hands are shaking."
"He used to be so awkward."
"I'm being hugged... I haven't felt this in so long."
"I have to stop tears from welling in my eyes."
"Not in front of my soldiers. Please..."
"When we finally part, I have to still hold on to his arm to believe he's real."
"The questions come flooding out before I can fully form them."
t "How long have you... what happened to... how did this happen?"
"Others emerge from the huts and the trees - humans and non. I see two other soldiers. I don't know them by name, but I recognize their faces."
"They join our circle, greeting me with the same warmth as Hector."
h "You probably know by now that time doesn't mean much out here."
show hector old concerned
h "We have no idea how long it's been."
h "I know we were left here about a month after you were..."
show hector old sad
h "But we have no idea where the ark has gone. I'm sorry."
t "No, don't feel bad. It's just... it's just so good to see you."
t "And who are these... these friends of yours?"
"The creature looks a little taken aback at my words."
"I can tell from its expression that it understands not only the language, but the tone of my voice."
show hector old happy
h "When we first got here, we fought with them."
h "They stole our supplies. We thought they were getting ready to kill us..."
h "But it was a misunderstanding. It sounds weird, but stealing is their way of an introduction."
"He laughs, but there's sadness in it."
h "There were a lot of misunderstandings at first."
h "But we resolved them."
h "We started to learn about each other."
h "When we realized the ark wasn't coming for us, they were all we had."
h "We made this garden for them. They protect us and keep us healthy, and we help them with what they need."
"The other soldiers have bundles on their back, I notice. When they see me staring quizzically at them, one of them turns around."
"Eight tiny legs sprout out from the bundle - and a small head."
"It's a baby. One of their babies."
t "You raise their children?"
h "It's dangerous to be a child for them. They grow quickly, but there's risk of theft by other clans. It can cause serious disputes."
h "So they protect us, and we protect them."
"Everyone looks so calm here. Even the creatures - strong and elegant as they seem - look relieved."
t "I'm happy for you, Hector."
show hector old neutral
h "And what about you, commander? You look exhausted."
t "Me? I guess it's a bit of a long story by now..."
if calypso1:
   t "I crash-landed on the planet in the debris field."
   t "I was lucky - the creature living there helped me rebuild my ship and leave."
else:
   t "I crashed on the planet in the debris field... and I met someone there who helped me."
   t "If it weren't for them, I would have died. They helped me rebuild my ship and leave the planet."
t "I went to another one of the planets the ark had marked as potentially inhabitable."
if green1:
   t "There was a civil war starting among the species there, and I got caught up in it."
   if okbreak:
      t "They were... incredible. They were - their culture, I mean."
      t "For a moment, I think I wanted to stay."
   if missyou:
      t "I left part of my heart there."
      t "If I could, I'd go back. But I have to find Penelope."
else:
   t "I met a family there. Helped them build a home."
   if childhome:
      t "It reminded me of Earth. Of what we've lost."
   else:
      t "It reminded me of what I want to build with Penelope. Wherever we end up."
t "I left, and went to another planet marked by the ark..."
if green2:
   t "There was a civil war going on among the species there, and I landed in the middle of it."
   if killscout:
      t "I killed someone."
      t "They were going to do something terrible."
      t "Maybe I didn't know enough about their culture..."
      t "But I couldn't just watch it happen. So I stopped them."
   else:
      t "I stumbled onto some political machinations. I had a hard choice to make."
      t "I still don't know if I made the right one."
else:
   t "I met a family there. They'd built a home, but it was crumbling."
   if inform:
      t "The son was deeply disturbed. I don't know what they did about it, but I told them."
   else:
      t "I think they were having trouble. I didn't want to intrude."
      t "I hope they're alright..."
t "Then I came here."
t "It sounds kind of funny when I say it all in a row like that."
"I can't help but smile, but Hector must see the pain in my expression, because he puts a hand on my shoulder."
h "You've made some hard decisions."
h "And all through it, you've kept looking for your daughter..."
h "She should be proud of you, Commander. If you'll permit me to say so."
t "Thank you."
"The other soldiers return to their work tending the garden, while the creature leaps back into the tree and climbs upward until I lose sight of it."
hide friend light
h "I understand, you know."
show hector old concerned
h "I understand making hard choices."
h "There was a time when I thought I'd break under the weight of the choices I made."
h "But I've learned to live with them."
h "It's all we can do in this life."
t "What did you do?"
"The question sounds ham-handed when I say it, but the intention behind it is honest. He listened to me unload my story. It's only fair I let him do the same."
h "A few of our men disagreed with settling down here."
h "They wanted to look for spare parts and make a new ship."
t "It's all woods here, right? There's no way you could find a ship in this."
"Hector shakes his head."
h "I told you about how our friends like to steal to introduce themselves, right? Well, they've stolen some big things before."
h "Like a shuttle. A working shuttle. With enough power to get us to wherever the ark is."
t "It sounds like it should have been gift-wrapped."
show hector old happy
"He chuckles at that."
show hector old concerned
h "Well, it's against their rules to give things away, except to their original owners."
h "Tran found out they had it. They wouldn't give it to him. So he tried to kill them to get it."
h "And they killed him."
h "When my men found out that story, a couple of them wanted to finish what he started. They would have started a war. We probably would have died."
h "And our friends were offering peace and assistance."
h "I wish it had been a harder choice. But to get what I have now... it was barely a choice at all."
h "I guess what I'm saying is - I learned a lot about myself that day. I looked at myself and I knew what choice I had to make."
h "I'm sure you feel the same."
t "You're saying you -"
t "You killed them? Your own people?"
show hector old angry
h "Yes. That's exactly what I did."
h "I took them out into the meadow early one morning and I shot them in the head, one by one."
h "I buried their bodies myself, and I made peace."
h "And look what I've built."
menu:
   "My reaction is instant and instinctual."
   "I am revolted.":
      $ revolted = True
      "The choice is not what bothers me..."
      "It's his expression that makes my stomach turn."
      t "How could you treat it that coldly?"
      t "These are your men's lives."
      t "I would never think of them so dismissively."
      h "You..."
      show hector old concerned
      h "I should have known you'd say that."
      h "It would have been nice to have your approval for once, commander."
      h "I always looked up to you."
      h "But it's alright."
      h "I've done what I had to do."
   "I understand.":
      $ understand = True
      "I know that choice."
      "I've never told anyone, but I remember that choice."
      "I wonder if he sees that in my eyes when I look into his right now."
      t "I understand."
      t "I'm sorry you had to make that choice."
      t "But you're right - look what you've built."
      t "It's beautiful."
      show hector old happy
      h "...Thank you."
      h "I can't express how much that means to me, commander."
label after_revoltmenu:
show hector old sad
h "Can you do something for me, commander? One last favor for a soldier?"
t "What is it?"
h "Can you tell the ark that we're dead?"
"The request catches me off-guard."
t "I could just tell them you don't want to be bothered..."
h "I don't know if they'll understand that. Maybe some of them will, but I don't want to risk anyone else looking for us."
h "This is our home now. We want to leave the ark behind us."
if calypso1:
   "It's hard for me to understand what they're saying, and when I try to think about it, it hurts."
   "But they're happy here. They've made a home. That much I can understand."
else:
   "A part of me - a part I've tried to silence since I found Calypso - a part of me envies them."
   "The burdens they carried on the ark - the burdens of a planet destroyed, the burdens of a terrible and tragic legacy - those burdens are gone now."
   "When I think about it, I'd give so much to have made the same choice."
t "Of course."
t "How did you die?"
h "The shuttle exploded on impact. We died in the wreckage."
h "It shouldn't be hard for them to believe. When we first landed, the beacon mistakenly said we'd died on landing. It's the story they think is true already."
t "That's all?"
h "Don't embellish it, commander."
h "We don't want to be heroes. We don't need to be remembered."
t "...Alright."
t "That's what I'll tell them."
h "Thank you. Truly."

scene bg jungle-night
with Dissolve(2.0)

"It's a little late for me to head out, so I spend the rest of the day with Hector's men tending to the garden."
"We harvest and forage some local foods, and the soldiers show me how to cook it on the fire."
"For dinner, we eat a long, chewy stalk that tastes remarkably like a hot dog, and a grilled mixture of spores, greens and mushrooms that is tangy, sweet and pungent all at once."
"The creatures make a preserved drink from spores collected from the canopy."
"It has an effect a little like alcohol, though a bit milder - a pleasant buzz I haven't felt comfortable feeling in a long time."
"Everyone is surprised when, in the midst of dinner, I turn my universal translator on and hold a conversation with the creatures."
"I let Hector borrow it after dinner and he walks off with one of them."
"They sit at the edge of the camp for a long time talking."
"When he finally comes back, I'm already in a bed they've made up for me from leaves and an old sleeping bag."
"I'm at the edge of sleep, but our eyes meet as he steps in the door."
if revolted:
   "I look away and roll over."
if understand:
   "I nod to him. He returns the gesture."
"He leaves the translator by my bag, and tucks into bed."

scene bg jungle-day
with Dissolve(2.0)

"The next day, everyone - including at least ten of the creatures - comes out to say goodbye."
"As I reach the top of the hill, I turn back to look at them."
if revolted:
   "They truly do look happy. {i}Look what I've built,{/i} Hector said. But at what cost?"
   "What choices have I found too easy, I wonder?"
   "Why did I react so badly to what he said?"
if understand:
   "They truly do look happy."
   "I'm proud of them."
   "I don't know if I affected them at all as their superior officer - or even if that matters now, in a different world with none of the people we knew -"
   "But I let myself feel that pride for just a moment."
"I make it back to the ship, and watch for the camp out the window as I fly up past the trees and back to the sky."
"It's a tiny dot, a multicoloured shock among sheets of pink and yellow-green."
"I watch it until it disappears beneath the clouds."

scene bg space
with Dissolve(2.0)

"And then I'm in space again."
"The silence is oppressive."

jump space4

label space4:

"I have nowhere else to go."
"The thought - cold, logical, factual - comes before the feeling of it."
"I turn off the screens and look out at the stars."
"I wasn't lying to Penelope before."
"I really haven't seen so many stars in my whole life."
"I don't think I'm ever going to get used to the sight."
"My stomach grumbles. I'm getting hungry."
"I have to go into stasis soon, or land somewhere..."
if calypso1:
   "I could always return to Calypso. But that feels like going backwards."
   "I can't go back now, not after so long."
else:
   "I could always return to Calypso."
   "The thought lingers in the back of my mind."
   "But I should consider other options first."
if missyou:
   "For a second, the thought of returning to Scout crosses my mind."
   "But that would be giving up on Penelope..."
   "It wouldn't be fair to her to do that. Or to them."
if understand:
   "I could join my soldiers..."
   "But they wanted me to think of them as dead."
   "I might be happy there, but I am not welcome there."
"I keep reaching for the controls and retreating at the last second."
"I have nowhere to go."
"I have nowhere to go."
"I have nowhere to go."
"I have nowhere..."
"Tears roll down my cheeks."
"I let out a sob... and another, and another."
"I bury my face in my hands."
"Is this really the end of it?"
"To drift into nothingness in space?"
"Penelope..."
if $calypso1:
   "I wish I could see you just once more."
else:
   "I'm so sorry I failed you."

scene bg black
with Dissolve(3.0)

"...REPEAT. THIS IS THE ARK."
"WE HAVE LANDED. WE ARE DISTRIBUTING COORDINATES."
"THIS IS THE ARK. FOR ANYONE ON THIS FREQUENCY SEARCHING FOR THE REMAINS OF HUMANITY..."
"COME TO THESE COORDINATES. WE HAVE LANDED."

scene bg space
with Dissolve(2.0)

"I bolt upright."
"I must have dozed off... but the message is coming through."
"I'm receiving the coordinates..."
"And I have them."
"A red dot appears on the map."
"The tears don't stop as I punch in the coordinates. I make sure they're exactly right, and then I bring the ship to its highest speed."
"The stars fly past us in so many tiny streams of light."
"I watch them for a long time."
"There's no way I can go into stasis now..."
"But I must. The coordinates are so far away."
"I try not to think about how long it'll take to get there."
"I recline in the chair."
"My eyes are wide open until the drugs from the stasis pod overtake me. Even then, I fight them as hard as I can."
"Penelope."
"Penelope..."
"I'm coming."
"I'm almost home."

scene bg black
with Dissolve(2.0)

t "I'm coming, Penelope."
t "I'll be there soon."
p "Are you, mom?"
p "Do you really want to come back?"

if desperate:
   p "Or do you just want to be loved?"
   p "Even if you think nothing of the people around you..."
   p "You'd rather be loved and miserable than forgotten and happy, wouldn't you?"

if lonely:
   p "Or is it just that you don't want to be alone?"
   p "Is it really better to hate everyone around you?"
   p "Even your own daughter?"
   p "Or is it better to be alone?"

if burial:
   p "Or do you just want to die?"
   p "To be buried with other humans?"
   p "Do you even want to live with us?"
   p "Do you even want to see me?"

if leavebe:
   p "Or do you just want us to know you're still alive?"
   p "Do you even care how we're doing?"
   p "Do you even care what happens after you get back?"

if revolted:
   p "Or do you just want to be in control?"
   p "You won't admit it to yourself..."
   p "But you don't believe we're alive, do you?"
   p "It's unthinkable that we would have lived without you, isn't it?"

if understand:
   p "Or do you just want to be validated?"
   p "To feel like the choices you've made have been the right ones?"
   p "To have someone tell you it's all going to be okay?"

p "You don't want to come back, mom."
p "You can still turn back now."
p "Wake up. Go back."
p "Find a new home."

"I try to wake up... but stasis holds me in place."

t "I'm sorry. I can't."

"But Penelope is gone."
"I am alone."
"Stasis is excruciatingly empty and cold."

scene bg space
with Dissolve(2.0)

"I wake up with a start."
"I am immediately awake."
"The ship is bright with the light of the planet above us."
"It is a swirling mess of puffy white clouds and bright blue oceans."
"I waste no time looking at it. I check the ship's readings, find the ark's coordinates and accelerate towards the planet's atmosphere."
"I'm going so fast that the ship rumbles and bumps as I descend."
"I barely notice."
"I pass into the clouds and everything around me is white..."
"And then the cliffs come into view below me."
"Before I can react they are all around me."
"I push hard on the breaks, but the ship hits ground before I can bring it to a stop."
"There is a loud screech, and I fall out of the seat."
"And all is quiet."
"I take a breath. It is long, shaking, and afraid."
"Then I open the hatch."

scene bg cliffs
with Dissolve(2.0)

"Green cliffs, carved as if by some intelligent hand, melt into white and blue."
"A flock of birds passes above me - they must be at least ten feet long."
"They have long, silver tails."
"This planet is beautiful."
"As I watch the birds fly off into the horizon, something catches the corner of my eye."
"It's an impact crater..."
"A trail..."
"Debris..."
"And a town, built from the remains of the ark."
"The ark."
"I'm so far away - and the shuttle's energy core is depleted."
"I have to walk."
"I don't care."
"I walk."
"The descent is difficult. My feet hurt from the blisters."
"But I don't take my eyes off of the ark."
"Finally it's right in front of me."
"I stand just behind a tree, just out of sight."
"I see families. Happy people."
"I can't even process their faces, my heart is beating so fast."
"But one jumps out at me: one figure, smaller than the others, standing on her own."
"The brown hair... the grey shirt..."
t "Penelope."
t "Penelope..."
t "Penelope!"
"I run to her."
"Spin her around."

show penelope neutral

t "Penelope!"

pause(2.0)

g "I'm not Penelope."
"...What?"
"But she looks just like her."
"Was there another child on the ark?"
"I wasn't aware -"
t "Where's Penelope?"
show penelope confused
g "I think she's over there."
show penelope sad
g "I don't know if you should go, though."
g "She doesn't want to see strangers right now."
t "It's okay. I'm not a stranger. I'm..."
"I follow the direction she's pointing."
"About twenty people are gathered around something."
"Is she in the crowd?"
"There are children in the crowd, but they're all smaller than her."
"I search their faces, but none of them are her."
"They don't notice me as I walk around them, craning my neck to see what they're all looking at."
"It's a bed. They're looking at a bed."
"I barely see the person inside the bed at first."
"There are so many people bent over her, holding her hands and crying."
"It's those hands I see first."
"They are old and wrinkled."
"And then I see her face..."
if calypso1:
   "All this time, I was so hopeful..."
else:
   "All this time, I've been so stupid..."
"My legs collapse under me."
"Penelope."

pause(3.0)

"The group starts to disperse."
"They're crying, holding each other. None of them notice me."
"From here, I can't tell if she's asleep or dead."
"But she's all alone."
"She's alone, and so am I."
menu:
   "I go to her.":
     "I pick myself up."
     "I put one foot forward..."
     "And another."
     "I reach her bedside."
     "I reach out for her hand."
     t "Penelope..."
     t "Penelope, I'm back."
     jump end
   "I leave.":
     "I pick myself up."
     "I put one foot forward..."
     "And another."
     "I turn from her."
     "I walk until I can no longer feel my feet."
     jump end

label end:
scene bg black
with Dissolve(3.0)
return
