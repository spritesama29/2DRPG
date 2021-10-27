#Kyle Stearns
#Player from https://opengameart.org/content/animated-rogue-extra
#Sounds from https://opengameart.org/content/horror-sound-effects-library
#Grey NPC from https://opengameart.org/content/ghost-1
#Dog from https://opengameart.org/content/hell-hound-character
#Monsters From User https://opengameart.org/users/dogchicken
#Fire from https://opengameart.org/content/lpc-flames
#Yellow Lightning From https://opengameart.org/content/rpg-special-move-effects
# Hammer From https://opengameart.org/content/heavy-iron-hammer
# Knife From https://opengameart.org/content/knife-4
#Chain Boots From https://opengameart.org/content/chain-boots-remix
#The method for animating most sprites except the Dog was learned from looking at the AnimatedWalkingSprite section of the Python Arcade website
import arcade
import pathlib





class Player(arcade.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.playerWidth = 32
        self.playerHeight = 44
        self.faceRight = True
        self.faceLeft = False
        self.faceUp = False
        self.faceDown = False
        self.score = 0
        self.strength = 3
        self.speed = 1
        self.currentDirection = self.faceRight
        self.currentTexture = 0
        self.scale = 1.5
        self.hasKnife=False
        self.hasHammer =False
        self.hasBoots=False
        self.inventorySlots = 0
        self.attacking = False
        self.frameSpeed =0
        playerAnPath = pathlib.Path.cwd() / 'Assets' / 'RogueGuy.png'
        self.walkRightTextures = []
        self.walkLeftTextures = []
        self.walkUpTextures = []
        self.walkDownTextures = []
        self.attackRightTextures = []
        self.attackLeftTextures = []
        for count in range(8):
            wRframe = arcade.load_texture(playerAnPath,count*self.playerWidth,self.playerHeight * 2,height=self.playerHeight,width=self.playerWidth)
            self.walkRightTextures.append(wRframe)
        for count in range(8):
            wLframe = arcade.load_texture(playerAnPath,count*self.playerWidth,self.playerHeight * 2,height=self.playerHeight,width=self.playerWidth,flipped_horizontally=True)
            self.walkLeftTextures.append(wLframe)
        for count in range(8):
            wUframe = arcade.load_texture(playerAnPath,count*self.playerWidth,self.playerHeight,height=self.playerHeight,width=self.playerWidth)
            self.walkUpTextures.append(wUframe)
        for count in range(8):
            wDframe = arcade.load_texture(playerAnPath,count*self.playerWidth,0,height=self.playerHeight,width=self.playerWidth)
            self.walkDownTextures.append(wDframe)
        for count in range(7):
            attackFrame = arcade.load_texture(playerAnPath,count*self.playerWidth,self.playerHeight * 3,height=self.playerHeight,width=self.playerWidth)
            self.attackRightTextures.append(attackFrame)
        for count in range(7):
            attackFrame = arcade.load_texture(playerAnPath,count*self.playerWidth,self.playerHeight * 3,height=self.playerHeight,width=self.playerWidth,flipped_horizontally=True)
            self.attackLeftTextures.append(attackFrame)




        #idle starting texture
        self.texture = self.walkRightTextures[0]


    def update_animation(self, delta_time: float = 1 / 60):

        if self.frameSpeed<2:
            self.frameSpeed += 1


            pass

        else:

            self.frameSpeed=0
            if (self.attacking == True and self.faceRight==True):

                self.currentTexture += 1
                self.change_x=0
                self.change_y=0
                if self.currentTexture > 6:
                    self.currentTexture = 0
                    self.attacking = False

                self.texture = self.attackRightTextures[self.currentTexture]


            elif (self.attacking == True and self.faceLeft==True):
                self.currentTexture += 1

                self.change_x = 0
                self.change_y = 0
                if self.currentTexture > 6:
                    self.currentTexture = 0
                    self.attacking = False
                self.texture = self.attackLeftTextures[self.currentTexture]
            elif self.change_x ==0 and self.change_y==0:
                self.texture=self.texture

            else:
                if(self.change_x>0):
                    self.faceRight=True
                    self.faceLeft=False
                    self.currentTexture +=1
                    if self.currentTexture>7:
                        self.currentTexture=0
                    self.texture = self.walkRightTextures[self.currentTexture]
                elif(self.change_x<0):
                    self.faceRight = False
                    self.faceLeft = True
                    self.currentTexture += 1
                    if self.currentTexture > 7:
                        self.currentTexture = 0
                    self.texture = self.walkLeftTextures[self.currentTexture]
                elif (self.change_y < 0):
                    self.currentTexture += 1
                    if self.currentTexture > 7:
                        self.currentTexture = 0
                    self.texture = self.walkDownTextures[self.currentTexture]
                elif (self.change_y > 0):
                    self.currentTexture += 1
                    if self.currentTexture > 7:
                        self.currentTexture = 0
                    self.texture = self.walkUpTextures[self.currentTexture]

class Skull(arcade.Sprite):
    def __init__(self):
        super(Skull, self).__init__()
        self.skullHeight =64
        self.skullWidth = 64
        NPCAnPath = pathlib.Path.cwd() / 'Assets' / 'skullGuy.png'
        self.attackingLeft =False
        self.faceRight = True
        self.faceLeft = False
        self.death = False
        self.scale = 1
        self.speed=1
        self.scoreReduction =50
        self.health = 25
        self.currentTexture = 0
        self.frameSpeed=0
        self.walkRightTextures = []
        self.walkLeftTextures = []
        self.attackLeftTextures = []
        self.deathTextures = []
        for count in range(4):
            wRframe = arcade.load_texture(NPCAnPath,count*self.skullWidth,self.skullHeight,height=self.skullHeight,width=self.skullWidth)
            self.walkRightTextures.append(wRframe)
        for count in range(4):
            wLframe = arcade.load_texture(NPCAnPath,count*self.skullWidth,self.skullHeight,height=self.skullHeight,width=self.skullWidth, flipped_horizontally=True)
            self.walkLeftTextures.append(wLframe)
        for count in range(4):
            attackFrame = arcade.load_texture(NPCAnPath,count*self.skullWidth,self.skullHeight*2,height=self.skullHeight,width=self.skullWidth, flipped_horizontally=True)
            self.attackLeftTextures.append(attackFrame)
        for count in range(7):
            deathFrame = arcade.load_texture(NPCAnPath,count*self.skullWidth,self.skullHeight*3,height=self.skullHeight,width=self.skullWidth, flipped_horizontally=True)
            self.deathTextures.append(deathFrame)
        self.texture = self.walkRightTextures[0]


    def update_animation(self, delta_time: float = 1 / 60):
        if self.frameSpeed<5:
            self.frameSpeed += 1


            pass
        else:
            self.frameSpeed=0
            if self.death==True:
                self.change_x=0
                self.currentTexture +=1
                if self.currentTexture > 6:
                    self.currentTexture = 0
                    self.remove_from_sprite_lists()

            self.texture = self.deathTextures[self.currentTexture]
            if self.attackingLeft==True:
                self.change_x=0
                self.currentTexture += 1
                if self.currentTexture > 3:
                    self.currentTexture = 0
                    self.attackingLeft=False

                self.texture = self.attackLeftTextures[self.currentTexture]
            elif (self.change_x > 0):
                self.faceRight=True
                self.faceLeft=False
                self.currentTexture += 1
                if self.currentTexture > 3:
                    self.currentTexture = 0
                self.texture = self.walkRightTextures[self.currentTexture]
            elif (self.change_x < 0):
                self.faceRight=False
                self.faceLeft=True
                self.currentTexture += 1
                if self.currentTexture > 3:
                    self.currentTexture = 0
                self.texture = self.walkLeftTextures[self.currentTexture]
class flyingMonster(arcade.Sprite):
    def __init__(self):
        super(flyingMonster, self).__init__()
        self.flyHeight =64
        self.flyWidth = 64
        NPCAnPath = pathlib.Path.cwd() / 'Assets' / 'tongueGuy.png'
        self.attackingLeft =False
        self.faceRight = True
        self.faceLeft = False
        self.death = False
        self.scale = 2
        self.speed=1
        self.scoreReduction =10
        self.health = 75
        self.currentTexture = 0
        self.frameSpeed=0
        self.walkRightTextures = []
        self.walkLeftTextures = []
        self.attackLeftTextures = []
        self.deathTextures = []
        for count in range(4):
            wRframe = arcade.load_texture(NPCAnPath,count*self.flyWidth,0,height=self.flyHeight,width=self.flyWidth)
            self.walkRightTextures.append(wRframe)
        for count in range(4):
            wLframe = arcade.load_texture(NPCAnPath,count*self.flyWidth,0,height=self.flyHeight,width=self.flyWidth, flipped_horizontally=True)
            self.walkLeftTextures.append(wLframe)
        for count in range(4):
            attackFrame = arcade.load_texture(NPCAnPath,count*self.flyWidth,self.flyHeight,height=self.flyHeight,width=self.flyWidth, flipped_horizontally=True)
            self.attackLeftTextures.append(attackFrame)
        for count in range(5):
            deathFrame = arcade.load_texture(NPCAnPath,count*self.flyWidth,self.flyHeight*2,height=self.flyHeight,width=self.flyWidth)
            self.deathTextures.append(deathFrame)
        self.texture = self.walkRightTextures[0]


    def update_animation(self, delta_time: float = 1 / 60):
        if self.frameSpeed<7:
            self.frameSpeed += 1


            pass
        else:
            self.frameSpeed=0
            if self.death==True:
                self.change_x=0
                self.currentTexture +=1
                if self.currentTexture > 4:
                    self.currentTexture = 0
                    self.remove_from_sprite_lists()

                self.texture = self.deathTextures[self.currentTexture]
            if self.attackingLeft==True:
                self.change_x=0
                self.currentTexture += 1
                if self.currentTexture > 3:
                    self.currentTexture = 0
                    self.attackingLeft=False

                self.texture = self.attackLeftTextures[self.currentTexture]
            elif (self.change_x > 0):
                self.faceRight=True
                self.faceLeft=False
                self.currentTexture += 1
                if self.currentTexture > 3:
                    self.currentTexture = 0
                self.texture = self.walkRightTextures[self.currentTexture]
            elif (self.change_x < 0):
                self.faceRight=False
                self.faceLeft=True
                self.currentTexture += 1
                if self.currentTexture > 3:
                    self.currentTexture = 0
                self.texture = self.walkLeftTextures[self.currentTexture]
class NPC(arcade.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.NPCwidth =32
        self.NPCheight =32
        self.frameSpeed = 0
        NPCAnPath = pathlib.Path.cwd() / 'Assets' / 'Ghost.png'
        self.scale = 1.5
        self.currentTexture = 0

        self.idleTextures = []

        for count in range(10):
            idleFrame = arcade.load_texture(NPCAnPath,count*self.NPCwidth,0,height=self.NPCheight,width=self.NPCwidth,flipped_horizontally=True)
            self.idleTextures.append(idleFrame)

        self.texture = self.idleTextures[0]
    def update_animation(self, delta_time: float = 1 / 60):
        if self.frameSpeed < 2:
            self.frameSpeed += 1
        else:
            self.frameSpeed = 0
            self.currentTexture+=1
            if self.currentTexture>9:
                self.currentTexture=0
            self.texture = self.idleTextures[self.currentTexture]

class Plant(arcade.Sprite):
    def __init__(self):
        super(Plant, self).__init__()
        self.plantWidth =64
        self.plantHeight = 64
        self.scale=1.5
        self.death=False
        self.attacking =False
        self.frameSpeed =0
        self.scoreReduction =0
        self.currentTexture=0
        self.health =100
        plantPath = pathlib.Path.cwd() / 'Assets' / 'plant.png'
        self.idleTextures = []
        self.attackingTextures = []
        self.deathTextures = []
        for count in range(3):
            idleFrame = arcade.load_texture(plantPath,count*self.plantWidth,0,height=self.plantHeight,width=self.plantWidth)
            self.idleTextures.append(idleFrame)
        for count in range(5):
            attackFrame = arcade.load_texture(plantPath,count*self.plantWidth,2*self.plantHeight,height=self.plantHeight,width=self.plantWidth)
            self.attackingTextures.append(attackFrame)
        for count in range(6):
            deathFrame = arcade.load_texture(plantPath,count*self.plantWidth,4*self.plantHeight,height=self.plantHeight,width=self.plantWidth)
            self.deathTextures.append(deathFrame)
        self.texture=self.idleTextures[0]
    def update_animation(self, delta_time: float = 1 / 60):
        if self.frameSpeed<12:
            self.frameSpeed += 1
            self.scoreReduction=0

            pass

        else:
            self.frameSpeed = 0
            if self.death==True:

                self.currentTexture +=1
                if self.currentTexture > 5:
                    self.currentTexture = 0
                    self.remove_from_sprite_lists()

                self.texture = self.deathTextures[self.currentTexture]
            elif self.attacking==True:


                self.currentTexture += 1

                if self.currentTexture > 4:
                    self.currentTexture = 0
                    self.attacking = False
                    self.scoreReduction=200

                self.texture = self.attackingTextures[self.currentTexture]
            else:
                self.currentTexture += 1
                if self.currentTexture > 2:
                    self.currentTexture = 0
                self.texture = self.idleTextures[self.currentTexture]
class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(800,800, "2D RPG Window")

        self.player_sprite = None
        self.playerFrameList = None

        self.player_path = pathlib.Path.cwd()/'Assets'/'RogueGuy.png'
        self.player = None
        self.starting1 = pathlib.Path.cwd()/'Assets'/'starting1.json'
        self.starting1WallList = None

        self.startingRight = pathlib.Path.cwd()/'Assets'/'startingRight.json'
        self.startingRightWallList = None

        self.tPath = pathlib.Path.cwd()/'Assets'/'tPath.json'
        self.tPathWallList = None

        self.underT = pathlib.Path.cwd()/'Assets'/'tUnder.json'
        self.underTWallList = None

        self.town = pathlib.Path.cwd()/'Assets'/'town.json'
        self.townWallList = None


        self.currentScene = None
        self.simple_physics = None
        self.simple_physics2 = None

        self.player = None
        self.player_list : arcade.SpriteList= None





    def setup(self):




        dogPath = pathlib.Path.cwd()/'Assets'/'dog.png'
        self.dogSprite = arcade.AnimatedTimeBasedSprite(dogPath, 2, image_width=64, image_height=32,center_x=75,center_y=100)
        dogChillFrames: list[arcade.AnimationKeyframe] = []
        for row in range(4):
            dogFrame = arcade.AnimationKeyframe(row, 300,
                                                 arcade.load_texture(str(dogPath), x=128 +(row * 64), y=0, width=64,
                                                                     height=32,flipped_horizontally=True))
            dogChillFrames.append(dogFrame)
        self.dogSprite.frames = dogChillFrames
        self.dogFrameList = arcade.SpriteList()
        self.dogFrameList.append(self.dogSprite)

        flamePath = pathlib.Path.cwd()/'Assets'/'flames.png'

        self.flameSprite = arcade.AnimatedTimeBasedSprite(flamePath, 4.5, image_width=16, image_height=24, center_x=463,
                                                          center_y=725)
        flameFrames: list[arcade.AnimationKeyframe] = []
        for row in range(3):
            flameFrame = arcade.AnimationKeyframe(row, 100,
                                                  arcade.load_texture(str(flamePath), x=16*row, y=0, width=16, height=24))
            flameFrames.append(flameFrame)
        self.flameSprite.frames = flameFrames
        self.flameFrameList = arcade.SpriteList()
        self.flameFrameList.append(self.flameSprite)

        lightPath = pathlib.Path.cwd() / 'Assets' / 'YellowJolt.png'
        self.lightSprite = arcade.AnimatedTimeBasedSprite(lightPath, .95, image_width=64, image_height=64, center_x=295,
                                                        center_y=715)
        lightFrames: list[arcade.AnimationKeyframe] = []
        for row in range(3):
            lightFrame = arcade.AnimationKeyframe(row, 100,
                                                arcade.load_texture(str(lightPath), x=64*row, y=0, width=64,
                                                                    height=64))
            lightFrames.append(lightFrame)
        self.lightSprite.frames = lightFrames
        self.lightSpriteFrames = arcade.SpriteList()
        self.lightSpriteFrames.append(self.lightSprite)

        #Sounds

        knife_path = pathlib.Path.cwd() / 'Assets' / 'Stab_Knife_00.mp3'
        self.knifeSound = arcade.load_sound(knife_path)

        zombie_path = pathlib.Path.cwd() / 'Assets' / 'Zombie_01.mp3'
        self.zombieSound = arcade.load_sound(zombie_path)

        deadZombie_path = pathlib.Path.cwd() / 'Assets' / 'Monster_00.mp3'
        self.deadZombieSound = arcade.load_sound(deadZombie_path)

        win_path = pathlib.Path.cwd() / 'Assets' / 'Jingle_Win_00.mp3'
        self.winSound = arcade.load_sound(win_path)
        self.winOver =0
        mint_path = pathlib.Path.cwd() / 'Assets' / 'Jingle_Achievement_00.mp3'
        self.mintSound = arcade.load_sound(mint_path)
        self.hasMintOver=0
        plantDeathSoundPath = pathlib.Path.cwd() / 'Assets' / 'Monster_01.mp3'
        self.plantDeathSound = arcade.load_sound(plantDeathSoundPath)

        tongueDeathPath = pathlib.Path.cwd() / 'Assets' / 'Monster_02.mp3'
        self.tongueDeathSound = arcade.load_sound(tongueDeathPath)

        mysteryPath = pathlib.Path.cwd() / 'Assets' / 'Evil_Machine_Loop_00.mp3'
        self.mysterySound = arcade.load_sound(mysteryPath)
        self.mysteryOver=0
        self.gui = arcade.Camera(self.width, self.height)
        self.gui = arcade.Camera(self.width,self.height)




        swordPath = pathlib.Path.cwd()/'Assets'/'knife.gif'
        self.knife = arcade.load_texture(swordPath)
        self.knifePickUp = arcade.Sprite()
        self.knifePickUp.texture = self.knife
        self.knifePickUp.scale = .2

        hammerPath = pathlib.Path.cwd()/'Assets'/'hammer.png'
        self.hammer = arcade.load_texture(hammerPath)
        self.hammerPickUp = arcade.Sprite()
        self.hammerPickUp.texture = self.hammer
        self.hammerPickUp.scale = 2

        bootsPath = pathlib.Path.cwd()/'Assets'/'chain_boots.png'
        self.boots = arcade.load_texture(bootsPath)
        self.bootsPickUp = arcade.Sprite()
        self.bootsPickUp.texture = self.boots
        self.bootsPickUp.scale = 1
        self.itemList = arcade.SpriteList()

        self.player = Player()
        self.player.center_x=200
        self.player.center_y=400

        self.player.attacking=False

        self.npc = NPC()
        self.npc.center_x =300
        self.npc.center_y = 400

        self.skull = Skull()
        self.skull.center_y=400
        self.skull.center_x=400
        self.skull.attackingLeft= False

        self.talking = False
        self.dogCount =0
        self.npcCount =0
        self.npcCount2 = 0
        self.questStart=False
        self.hasMint =False
        self.questDone=False
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.player_list.append(self.flameSprite)
        self.player_list.append(self.lightSprite)
        self.plant = Plant()
        self.plant.center_x =700
        self.plant.center_y = 400

        self.flyMon = flyingMonster()
        self.flyMon.center_x=500
        self.flyMon.center_y=400
        self.monsterList = arcade.SpriteList()

        self.starting1Map = arcade.tilemap.load_tilemap(self.starting1)
        self.starting1WallList = self.starting1Map.sprite_lists["Wall"]

        self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.starting1WallList)

        self.starting1Scene = arcade.Scene.from_tilemap(self.starting1Map)


        self.startingRightMap = arcade.tilemap.load_tilemap(self.startingRight)
        self.startingRightWallList = self.startingRightMap.sprite_lists["Walls"]
        self.startingRightScene = arcade.Scene.from_tilemap(self.startingRightMap)

        self.tPathMap = arcade.tilemap.load_tilemap(self.tPath)
        self.tPathWallList = self.tPathMap.sprite_lists["Walls"]
        self.tPathScene = arcade.Scene.from_tilemap(self.tPathMap)

        self.townMap = arcade.tilemap.load_tilemap(self.town)
        self.townWallList = self.townMap.sprite_lists["Walls"]

        self.townScene = arcade.Scene.from_tilemap(self.townMap)

        self.tUnderMap = arcade.tilemap.load_tilemap(self.underT)
        self.tUnderWallList = self.tUnderMap.sprite_lists["Walls"]
        self.tUnderScene = arcade.Scene.from_tilemap(self.tUnderMap)

        self.currentScene = self.starting1Scene

    def on_draw(self):
        arcade.start_render()

        self.currentScene.draw()
        self.player_list.draw()
        self.monsterList.draw()
        self.itemList.draw()

        self.gui.use()
        score = f"score: {self.player.score}"
        arcade.draw_text(
            score,
            50,
            700,
            arcade.color.WHITE,
            18,)
        speed = f"Speed: {self.player.speed}"
        arcade.draw_text(
            speed,
            200,
            700,
            arcade.color.PURPLE,
            18, )
        strength = f"Strength: {self.player.strength}"
        arcade.draw_text(
            strength,
            350,
            700,
            arcade.color.FLIRT,
            18, )
        inventory = f"Inventory slots used:{self.player.inventorySlots}/2"
        arcade.draw_text(
            inventory,
            525,
            700,
            arcade.color.WHITE,
            18, )
        if self.talking==True and self.npcCheck==True and self.npcCount==1:
            arcade.draw_text("Oh hello! How's it going?", 200, 425,
                         arcade.color.GREEN, 12, 80, 'left')
        elif self.talking==True and self.npcCheck==True and self.npcCount==2:
            arcade.draw_text(".........", 250, 425,
                         arcade.color.GREEN, 12, 80, 'left')
        elif self.talking==True and self.npcCheck==True and self.npcCount==3:
            arcade.draw_text("You want to...Go Fast?", 200, 425,
                         arcade.color.GREEN, 12, 80, 'left')
        elif self.talking==True and self.npcCheck==True and self.npcCount==4:
            arcade.draw_text("Well I might have something......for a favor", 200, 425,
                         arcade.color.GREEN, 12, 80, 'left')
        elif self.talking==True and self.npcCheck==True and self.npcCount==5:
            arcade.draw_text("You see, I'm awfully curious today so......", 200, 425,
                         arcade.color.GREEN, 12, 80, 'left')
        elif self.talking==True and self.npcCheck==True and self.npcCount==6:
            arcade.draw_text("Could you do me a favor and find out what the Dog doin'?", 200, 425,
                         arcade.color.GREEN, 12, 80, 'left')


        elif self.talking==True and self.npcCheck==True and self.hasMint==False:
            arcade.draw_text("Did you find out yet?", 250, 425,
                         arcade.color.GREEN, 12, 80, 'left')
        elif self.talking == True and self.npcCheck == True and self.npcCount2>=2:
            arcade.draw_text("You want more? Sorry that's DLC", 200, 500,
                             arcade.color.GREEN, 12, 80, 'left')

        elif self.talking == True and self.npcCheck == True and self.hasMint == True :
            arcade.draw_text("He's looking for mints??!That's the dumbest thing I've ever heard", 200, 500,
                             arcade.color.GREEN, 12, 80, 'left')
            arcade.draw_text("But fine, a deal's a deal", 250, 475,
                             arcade.color.GREEN, 12, 80, 'left')
            self.questDone=True

        elif self.talking==True and self.dogCheck==True and self.questStart==False:
            arcade.draw_text("Got nothing to say? leave me alone then"
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')

        elif self.talking==True and self.dogCheck==True and self.dogCount==1:
            arcade.draw_text("...What am I doin'? What kind of question is that?  "
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')
        elif self.talking==True and self.dogCheck==True and self.dogCount==2:
            arcade.draw_text("...I'm looking for  more mints to add to my collection"
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')
        elif self.talking==True and self.dogCheck==True and self.dogCount==3:
            arcade.draw_text(".................. "
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')
        elif self.talking==True and self.dogCheck==True and self.dogCount==4:
            arcade.draw_text("What?"
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')
        elif self.talking==True and self.dogCheck==True and self.dogCount==5:
            arcade.draw_text("You want a mint to prove what I'm Doin'?"
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')
        elif self.talking==True and self.dogCheck==True and self.dogCount==6:
            arcade.draw_text("Fine whatever please leave"
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')

            self.hasMint=True
        elif self.talking==True and self.dogCheck==True and self.dogCount>6:
            arcade.draw_text("I gave you the mint, now scram"
                             , 75, 125,
                             arcade.color.YELLOW_ROSE, 12, 80, 'left')

    def on_key_press(self, key: int, modifiers: int):
        if self.talking==True and self.dogCheck==True or self.talking==self.npcCheck==True:
            if key ==arcade.key.Z:
                self.talking=False

        else:
            if key == arcade.key.UP:
                if self.player.attacking==False:
                    self.player.change_y += self.player.speed
                else:
                    pass

            if key == arcade.key.DOWN:
                if self.player.attacking == False:
                    self.player.change_y -= self.player.speed

                else:
                    pass
            if key == arcade.key.LEFT:
                if self.player.attacking == False:
                    self.player.currentDirection="left"
                    self.player.change_x -= self.player.speed
                else:
                    pass
            if key == arcade.key.RIGHT:
                if self.player.attacking == False:
                    self.player.currentDirection="right"
                    self.player.change_x += self.player.speed
                else:
                    pass
            if key == arcade.key.X and self.player.change_x ==0 and self.player.change_y==0:
                self.player.currentTexture=0
                self.player.attacking=True
                arcade.play_sound(self.knifeSound)
            if key == arcade.key.Z and self.dogCheck==True:
                self.talking=True
                if self.questStart==True:
                    self.dogCount+=1
            if key == arcade.key.Z and self.npcCheck==True:
                self.talking=True
                self.npcCount+=1
                if self.hasMint==True:
                    self.npcCount2+=1
                else:
                    self.questStart = True


    def on_key_release(self, key: int, modifiers: int):
        if self.player.change_y < 0 and (key == arcade.key.DOWN):
            self.player.change_y = 0
        if self.player.change_y > 0 and (key == arcade.key.UP):
            self.player.change_y = 0
        if self.player.change_x < 0 and (key == arcade.key.LEFT):
            self.player.change_x = 0
        if self.player.change_x > 0 and (key == arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time: float):

        self.player_list.update()
        self.player_list.update_animation()
        self.townWallList.update()
        self.simple_physics.update()
        self.monsterList.update()
        self.monsterList.update_animation()

        self.npcCheck = arcade.check_for_collision(self.player, self.npc) and self.currentScene==self.townScene
        self.dogCheck = arcade.check_for_collision(self.player, self.dogSprite) and self.currentScene==self.tUnderScene
        self.skullCheck = arcade.check_for_collision(self.player,self.skull) and self.skull.death==False
        self.skullClose = 20>self.skull.center_x-self.player.center_x>0
        self.plantCheck = arcade.check_for_collision(self.player,self.plant) and self.plant.death==False
        self.plantClose = 30>self.plant.center_x-self.player.center_x>0
        self.flyCheck = arcade.check_for_collision(self.player,self.flyMon) and self.flyMon.death==False
        self.flyClose = 50>self.flyMon.center_x-self.player.center_x>0
        self.inventorySpace = self.player.inventorySlots<2
        #logic for picking up items
        if self.questDone==True and self.winOver==0:
            self.player.speed=7
            arcade.play_sound(self.winSound)
            self.winOver=1
        if self.questStart==True and self.mysteryOver==0:
            arcade.play_sound(self.mysterySound)
            self.mysteryOver=1
        if self.hasMint==True and self.hasMintOver==0:
            arcade.play_sound(self.mintSound)
            self.hasMintOver=1
        if arcade.check_for_collision(self.player,self.knifePickUp)==True and self.player.hasKnife==False and self.inventorySpace:


            self.player.hasKnife=True
            self.player.strength=4
            self.itemList.remove(self.knifePickUp)
            self.player.inventorySlots+=1
        if arcade.check_for_collision(self.player,self.hammerPickUp)==True and self.player.hasHammer==False and self.inventorySpace:
            self.player.hasHammer=True
            self.player.strength=10
            self.itemList.remove(self.hammerPickUp)
            self.player.inventorySlots += 1
        if arcade.check_for_collision(self.player,self.bootsPickUp)==True and self.player.hasBoots==False and self.inventorySpace:
            self.player.hasBoots=True
            self.player.speed=3
            self.itemList.remove(self.bootsPickUp)
            self.player.inventorySlots += 1
       #logic for skull enemy

        if self.player.attacking==True and self.skullClose and self.skull.death==False:
            self.skull.health = self.skull.health-self.player.strength

        if self.skull.health<0:
            if self.skull.death==False:
                self.player.score+=100
                arcade.play_sound(self.deadZombieSound)
            self.skull.death = True

            self.knifePickUp.center_x = self.skull.center_x
            self.knifePickUp.center_y = self.skull.center_y
        if self.skullCheck==True and self.player.faceRight==True and self.currentScene==self.startingRightScene:
            self.player.center_x= self.skull.center_x - 15
        if self.skullClose and self.skull.death==False and self.skull.faceLeft==True and self.currentScene==self.startingRightScene:
            self.skull.attackingLeft=True
            arcade.play_sound(self.zombieSound)
            self.player.center_x-=7
            self.player.change_x=0
            self.player.score-=self.skull.scoreReduction
        if self.skull.center_x <200 and self.skull.attackingLeft==False or self.skull.change_x==0:
            self.skull.change_x =.4
        elif self.skull.center_x >600 and self.skull.attackingLeft==False:
            self.skull.change_x =-2


        #Logic for flying monster
        if self.player.attacking==True and self.flyClose and self.flyMon.death==False and self.currentScene==self.tUnderScene:
            self.flyMon.health= self.flyMon.health - self.player.strength

        if self.flyMon.health<0:
            if self.flyMon.death==False:
                self.player.score+=400
                arcade.play_sound(self.tongueDeathSound)
            self.flyMon.death = True
            self.bootsPickUp.center_x = self.flyMon.center_x
            self.bootsPickUp.center_y = self.flyMon.center_y

        if self.flyClose and self.flyMon.death==False and self.flyMon.faceLeft==True and self.currentScene==self.tUnderScene:
            self.flyMon.attackingLeft=True
            self.player.center_x-=10
            self.player.change_x=0
            self.flyMon.center_x-=7
            self.flyMon.currentTexture=0
            self.player.score-=self.flyMon.scoreReduction
        if self.flyCheck==True and self.currentScene==self.tUnderScene:
            self.player.center_x-=7
        if self.flyMon.center_x >700 and self.flyMon.attackingLeft==False:
            self.flyMon.change_x =-1
        if self.flyMon.center_x <500 and self.flyMon.attackingLeft==False or self.flyMon.change_x==0:
            self.flyMon.change_x =.7

        #Logic for plant Monster
        if self.plant.health < 0:

            if self.plant.death == False:
                self.player.score += 200
                arcade.play_sound(self.plantDeathSound)
            self.plant.death=True
            self.hammerPickUp.center_x = self.plant.center_x
            self.hammerPickUp.center_y = self.plant.center_y
        if self.plantCheck==True and self.currentScene==self.tPathScene:
            self.player.center_x=self.plant.center_x-25
        if self.plantClose and self.plant.death==False and self.currentScene==self.tPathScene:

            self.plant.attacking=True

            self.player.score-=self.plant.scoreReduction
        if self.player.attacking==True and self.plantClose==True and self.plant.death==False:
            self.plant.health = self.plant.health - self.player.strength


        #Going to other Screen Logic

        if self.player.center_x >self.width and self.currentScene == self.starting1Scene:
            self.player.center_x = 0
            self.currentScene = self.startingRightScene
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.startingRightWallList)
            if self.skull.death==False:
                self.monsterList.append(self.skull)
                self.itemList.append(self.knifePickUp)
            if self.skull.death==True and self.player.hasKnife==False:
                self.itemList.append(self.knifePickUp)
        elif self.player.center_x < 0 and self.currentScene == self.startingRightScene:
            self.player.center_x = self.width
            self.currentScene = self.starting1Scene
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.starting1WallList)
            if self.player.hasKnife==False:
                self.itemList.remove(self.knifePickUp)
            if self.skull.death==False:
                self.monsterList.remove(self.skull)


        elif self.player.center_x >self.width and self.currentScene ==self.startingRightScene:
            self.player.center_x = 0
            self.currentScene = self.tPathScene
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.tPathWallList)
            if self.plant.death==False:
                self.monsterList.append(self.plant)
                self.itemList.append(self.hammerPickUp)
            if self.plant.death==True and self.player.hasHammer==False:
                self.itemList.append(self.hammerPickUp)
        elif self.player.center_x < 0 and self.currentScene == self.tPathScene:
            self.player.center_x = self.width
            self.currentScene = self.startingRightScene
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.startingRightWallList)
            if self.plant.death==False:
                self.monsterList.remove(self.plant)
                self.itemList.remove(self.hammerPickUp)
            if self.plant.death==True and self.player.hasHammer==False:
                self.itemList.remove(self.hammerPickUp)
        elif self.player.center_x > self.width and self.currentScene == self.tPathScene:
            self.player.center_x = 0
            self.currentScene = self.townScene
            self.player_list.append(self.npc)
            if self.player.hasHammer==False:
                self.itemList.remove(self.hammerPickUp)
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.townWallList)

        elif self.player.center_x < 0 and self.currentScene == self.townScene:
            self.player.center_x = self.width
            self.currentScene = self.tPathScene
            self.player_list.remove(self.npc)
            if self.player.hasHammer==False:

                self.itemList.append(self.hammerPickUp)
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.tPathWallList)
        elif self.player.center_y < 0 and self.currentScene ==self.tPathScene:
            self.player.center_y = self.height
            self.currentScene = self.tUnderScene
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.tUnderWallList)
            self.player_list.append(self.dogSprite)
            if self.flyMon.death==False:
                self.monsterList.append(self.flyMon)
                self.itemList.append(self.bootsPickUp)
            if self.flyMon.death==True and self.player.hasBoots==False:
                self.itemList.append(self.bootsPickUp)
            if self.plant.death==False:
                self.monsterList.remove(self.plant)
                self.itemList.remove(self.hammerPickUp)
            if self.plant.death == True and self.player.hasHammer == False:
                self.itemList.remove(self.hammerPickUp)
        elif self.player.center_y > self.height and self.currentScene == self.tUnderScene:
            self.player.center_y = 0
            self.currentScene = self.tPathScene
            self.simple_physics = arcade.PhysicsEngineSimple(self.player, self.tPathWallList)
            self.player_list.remove(self.dogSprite)
            if self.plant.death==False:
                self.monsterList.append(self.plant)

            if self.player.hasHammer==False:
                self.itemList.append(self.hammerPickUp)
            if self.player.hasBoots==False:
                self.itemList.remove(self.bootsPickUp)
            if self.flyMon.death==False:
                self.monsterList.remove(self.flyMon)
        elif self.npcCheck==True:
            if self.talking ==True:
                self.player.center_x = self.npc.center_x-10
            elif self.player.faceRight==True:
              self.player.center_x = self.npc.center_x-10

        elif self.dogCheck==True:
            self.player.center_x = self.dogSprite.center_x+55



def main():
    window = GameWindow()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()