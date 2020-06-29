import { Component, OnInit } from "@angular/core";
import { ImageData, ImageService } from "../image-data.service";
import { Observable, Subject } from "rxjs";
import { takeUntil } from "rxjs/operators";
import { MatDialog } from '@angular/material/dialog';

import 'hammerjs';


declare var myFunction;
declare var myTodayFunction;
declare var myLastWeekFunction;
declare var myOlderFunction;

@Component({
  selector: "app-webcam",
  templateUrl: "./webcam.component.html",
  styleUrls: ["./webcam.component.scss"],
})
export class WebcamComponent implements OnInit {


  Images: ImageData[] = [];
  ImageService: ImageService;
  destroyed: Subject<boolean>;
  panelOpenState = false;

  CallMyFunction() {
    myFunction();
    myTodayFunction();
    myLastWeekFunction();
    myOlderFunction();
    
  }

  constructor(ImageService: ImageService) {
    this.ImageService = ImageService;
  }

  ngOnInit() {
    this.ImageService.getImages()
     
      .subscribe((data) => {
        this.Images = data;
        console.log(this.Images);
        
      });

 

  }

  ngOnDestroy() {
    this.destroyed.next(true);
  }

  getImageLocation() {
    console.log(this.Images.map((data) => data.image));
    return this.Images.map((data) => data.image);
  }

  getImageDate() {
    console.log(this.Images.map((data) => data.measurement_time));
    return this.Images.map((data) => data.measurement_time);
  }



  
}

export class NgbdDropdownBasic {
  
}
