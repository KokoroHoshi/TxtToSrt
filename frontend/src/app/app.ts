import { Component, signal } from '@angular/core';
import { TxtToSrt } from './components/txt-to-srt/txt-to-srt';

@Component({
  selector: 'app-root',
  imports: [TxtToSrt],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('frontend');
}
