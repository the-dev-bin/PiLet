import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-pioutlet-status',
  templateUrl: './pioutlet-status.component.html',
  styleUrls: ['./pioutlet-status.component.scss'],
})
export class PioutletStatusComponent implements OnInit {

  dataStuffs = {};


  constructor(private http:HttpClient) {
    this.http.get("http://localhost:9000/active").subscribe(data => this.updateData(data));

   }

   updateData(stuff){
    this.dataStuffs = stuff;
    console.log(this.dataStuffs);
  }

  ngOnInit() {

  }

}
