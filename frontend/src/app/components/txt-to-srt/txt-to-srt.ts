import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from "@angular/forms";
import { HttpClient } from '@angular/common/http';

@Component({
  standalone: true,
  selector: 'app-txt-to-srt',
  imports: [CommonModule, FormsModule],
  templateUrl: './txt-to-srt.html',
  styleUrl: './txt-to-srt.scss',
})

export class TxtToSrt {
  textInput = '';
  selectedFile?: File;
  selectedFileName = '';
  convertedFileUrl?: string;
  isLoading = false;

  private apiUrl = 'http://localhost:8000/txt-to-srt';

  constructor(private http: HttpClient){}

  onFileSelected(event: any) {
    const file = event.target.files[0];

    if (file) {
      this.selectedFile = file;
      this.selectedFileName = file.name;
      this.textInput = '';
    }
  }

  onConvert() {
    this.isLoading = true;
    this.convertedFileUrl = undefined;

    let formData = new FormData();

    if (this.selectedFile) {
      formData.append('file', this.selectedFile);
    } else if (this.textInput.trim()) {
      formData.append('text', this.textInput.trim());
    } else {
      alert("Please paste your text or upload a text file 請貼上文字或上傳檔案");
    }

    this.http.post(this.apiUrl, formData, {responseType: 'blob'}).subscribe({
      next: (blob) => {
        this.isLoading = false;
        this.convertedFileUrl = URL.createObjectURL(blob);
      },
      error: (err) => {
        this.isLoading = false;
        alert('Convertion failed 轉換失敗： ' + err.message);
      },
    });
  }
}
