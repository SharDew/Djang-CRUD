// replace smart object’s content and save psd; 
// 2011, use it at your own risk; 
#target photoshop 
if (app.documents.length > 0) { 
var myDocument = app.activeDocument; 
var theName= myDocument.name.match(/(.*)\.[^\.]+$/)[1]; 
var thePath = myDocument.path; 
var theLayer = myDocument.activeLayer; 
// psd options; 
psdOpts = new PhotoshopSaveOptions(); 
psdOpts.embedColorProfile = true; 
psdOpts.alphaChannels = true; 
psdOpts.layers = true; 
psdOpts.spotColors = true; 
// check if layer is smart object; 
if (theLayer.kind != "LayerKind.SMARTOBJECT") {alert ("selected layer is not a smart object")} 
else { 
// select files; 
if ($.os.search(/windows/i) != -1) {var theFiles = File.openDialog ("please select files", "*.psd;*.tif;*.jpg", true)} 
else {var theFiles = File.openDialog ("please select files", getFiles, true)}; 
if (theFiles) { 
// work through the array; 
          for (var m = 0; m < theFiles.length; m++) { 
// replace smart object; 
                    theLayer = replaceContents (theFiles[m], theLayer); 
                    var theNewName = theFiles[m].name.match(/(.*)\.[^\.]+$/)[1]; 
//Raise color picker for Back cover; 
try { 
app.activeDocument.activeLayer = app.activeDocument.layers[app.activeDocument.layers.length - 1]; 
// ======================================================= 
var idsetd = charIDToTypeID( "setd" ); 
var desc7 = new ActionDescriptor(); 
var idnull = charIDToTypeID( "null" ); 
var ref2 = new ActionReference(); 
var idcontentLayer = stringIDToTypeID( "contentLayer" ); 
var idOrdn = charIDToTypeID( "Ordn" ); 
var idTrgt = charIDToTypeID( "Trgt" ); 
ref2.putEnumerated( idcontentLayer, idOrdn, idTrgt ); 
desc7.putReference( idnull, ref2 ); 
var idT = charIDToTypeID( "T   " ); 
var desc8 = new ActionDescriptor(); 
var idClr = charIDToTypeID( "Clr " ); 
var idsolidColorLayer = stringIDToTypeID( "solidColorLayer" ); 
desc7.putObject( idT, idsolidColorLayer, desc8 ); 
executeAction( idsetd, desc7, DialogModes.ALL ); 
} catch (e) {}; 
//save jpg; 
                    myDocument.saveAs((new File(thePath+"/"+theName+"_"+theNewName+".psd")),psdOpts,true); 
                    } 
          } 
} 
}; 
////// get psds, tifs and jpgs from files ////// 
function getFiles (theFile) { 
     if (theFile.name.match(/\.(psd|tif|jpg)$/i) != null || theFile.constructor.name == "Folder") { 
          return true 
          }; 
     }; 
////// replace contents ////// 
function replaceContents (newFile, theSO) { 
app.activeDocument.activeLayer = theSO; 
// ======================================================= 
var idplacedLayerReplaceContents = stringIDToTypeID( "placedLayerReplaceContents" ); 
    var desc3 = new ActionDescriptor(); 
    var idnull = charIDToTypeID( "null" ); 
    desc3.putPath( idnull, new File( newFile ) ); 
    var idPgNm = charIDToTypeID( "PgNm" ); 
    desc3.putInteger( idPgNm, 1 ); 
executeAction( idplacedLayerReplaceContents, desc3, DialogModes.NO ); 
return app.activeDocument.activeLayer 
};
