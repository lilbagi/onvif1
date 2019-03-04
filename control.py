def instlinfo(camera):
   #creating media, imaging services	
   camera.media_service = camera.create_media_service()
   camera.imaging_service = camera.create_imaging_service()
   #getting profiles
   camera.profiles = camera.media_service.GetProfiles()
   camera.media_profile = camera.profiles[0]
   #creating ptz setvice
   camera.ptz = camera.create_ptz_service()
   #getting videoSource token
   camera.vstoken = camera.media.GetVideoSources()[0]._token
   #getting notes about the posibilities of camera	
   camera.ptz.GetNodes()

def absolute_move(camera, x, y, zoom):
	#creating request for moving
	camera.request_absolute_move = camera.ptz.create_type("AbsoluteMove")
	camera.request_absolute_move.ProfileToken = camera.media_profile._token
	#printing status
	status = camera.ptz.GetStatus({"ProfileToken":camera.media_profile._token})
	print(status.Position)
	status.Position.PanTilt._x = x
	status.Position.PanTilt._y = y
	status.Position.Zoom._x = zoom
	camera.request_absolute_move.Position = status.Position
	#moving
	camera.ptz.AbsoluteMove(camera.request_absolute_move)	
#info about status(position, zoom)    
def get_status(camera):
	status = camera.ptz.GetStatus({"ProfileToken":camera.media_profile._token})
	return status.Position
#stop action
def stop(camera):
    camera.request_continuous_move.PanTilt = True
    camera.request_continuous_move.Zoom = True
    camera.ptz.Stop(camera.request_continuous_move)
    print ("Stopped")
	
def continuous_move(camera, mode, velocity, timeout):
    from time import sleep
    #creating request for moving
    camera.request_continuous_move = camera.ptz.create_type("ContinuousMove")
    camera.request_continuous_move.ProfileToken = camera.media_profile._token   
    #dif modes of moving  
    if mode == 'tilt':
        print("Move tilt")
        camera.request_continuous_move.Velocity.PanTilt._x = 0.0
        camera.request_continuous_move.Velocity.PanTilt._y = velocity
    if mode == 'pan':
        print ("Move pan")
        camera.request_continuous_move.Velocity.PanTilt._x = velocity
        camera.request_continuous_move.Velocity.PanTilt._y = 0.0
    if mode == 'zoom':
        print ("Zoom")
        camera.request_continuous_move.Velocity.Zoom._x = velocity
    camera.ptz.ContinuousMove(camera.request_continuous_move)
    #time to move
    sleep(timeout)
    #stopping
    stop(camera)
	
def absolute_focus(camera, x):
	#creating request for focusing
	camera.request_focus_change = camera.imaging.create_type("Move")
	camera.request_focus_change.VideoSourceToken = camera.media_profile.VideoSourceConfiguration.SourceToken
	camera.request_focus_change.Focus = {}
	camera.request_focus_change.VideoSourceToken = camera.vstoken
	#set the focus
	camera.request_focus_change.Absolute = {'Position': x}
	camera.imaging.Move(camera.request_focus_change)

def continuous_focus(camera, speed):
     #creating request for focusing
     camera.request_focus_change = camera.imaging.create_type("Move")
     camera.request_focus_change.VideoSourceToken = camera.media_profile.VideoSourceConfiguration.SourceToken
     camera.request_focus_change.Focus = {}
     camera.request_focus_change.VideoSourceToken = camera.vstoken
     #set speed to approach the focus
     camera.request_focus_change.Focus = {'Continuous': {'Speed': speed}}
     camera.imaging.Move(camera.request_focus_change)
     #stop focusing	
     camera.imaging.Stop({'VideoSourceToken': camera.vstoken})    		



    
    
